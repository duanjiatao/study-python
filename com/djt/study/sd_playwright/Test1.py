import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        # 打开浏edge览器
        browser = await p.chromium.launch(headless=False, channel="msedge")
        # 创建会话
        context = await browser.new_context()
        # 创建新标签页
        page = await context.new_page()
        # 打开百度
        await page.goto("http://www.baidu.com")
        # 打印页面标题
        print(await page.title())
        # 输入日期
        await page.fill("#kw", "日期")
        # 点击百度一下按钮
        await page.get_by_role("button", name="百度一下").click()

        await asyncio.sleep(10)

        # 关闭浏览器
        await context.close()
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
