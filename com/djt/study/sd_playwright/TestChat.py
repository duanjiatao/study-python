"""
使用playwright实现gpt对话
"""

import asyncio
import os

from playwright.async_api import async_playwright, Page

# 对话框计数
chat_count = 0


async def chat(question_list):
    """
    针对给出的问题，获取对应的回答
    :param question_list:问题列表
    :return:
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, channel='msedge')
        state_path = 'auth/chat.json'
        create_file(state_path)
        context = await browser.new_context(storage_state=state_path)
        page = await context.new_page()
        await page.goto('https://chat.jinshutuan.com')
        await page.wait_for_load_state(state='domcontentloaded')
        print(page.url)

        for question in question_list:
            print('问=>', question)
            await ask(page, question)
            print('答=>', await answer(page))
            print('=' * 100)

        await context.storage_state(path=state_path)

        # page.pause()
        await asyncio.sleep(5)
        await context.close()
        await browser.close()


async def ask(page: Page, text: str):
    """
    提问
    :param page:
    :param text:
    :return:
    """
    # 输入提问内容
    await page.fill('//*[@id="app"]/div/div[1]/div/div/div/div/div/div/footer/div/div[3]/div/div[1]/div[1]/textarea',
                    text)
    # 点击发送按钮
    await page.get_by_role("contentinfo").get_by_role("button").nth(4).click()
    # 等待停止按钮消失 说明回答完毕
    await page.wait_for_selector('#image-wrapper > div.sticky.bottom-0.left-0.flex.justify-center > button',
                                 state='hidden', timeout=60000)
    # 更新对话框编号
    global chat_count
    chat_count += 2


async def answer(page: Page) -> str:
    """
    获取回答
    :param page:
    :return:
    """
    return await page.text_content(f'//*[@id="image-wrapper"]/div[{chat_count}]/div[2]/div/div[1]/div/div')


def create_file(path: str):
    """
    创建空state文件
    :param path:
    :return:
    """
    if not os.path.exists(path):
        # 如果文件不存在，则创建一个空文件
        with open(path, 'w') as f:
            f.write('{"cookies":[],"origins":[]}')


if __name__ == '__main__':
    question_list = [
        '今天是几号',
        '介绍一下python',
        '你对人工智能的发展怎么看',
        '用java写一个快速排序'
    ]
    asyncio.run(chat(question_list))
