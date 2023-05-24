import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, channel="msedge")
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://mail.163.com/")
        for f in page.frames:
            print(f)

        await asyncio.sleep(10)
        # 关闭浏览器
        await context.close()
        await browser.close()


async def main2():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, channel="msedge", devtools=False)
        context = await browser.new_context()  # 创建上下文，浏览器实例

        page = await context.new_page()  # 打开标签页
        await page.goto("https://www.baidu.com/")
        print(page.title())
        # Get page after a specific action (e.g. clicking a link)
        async with context.expect_page() as new_page_info:
            await page.click('text=贴吧')  # Opens a new tab
        new_page = await new_page_info.value

        await new_page.wait_for_load_state()  # 等待页面加载到指定状态
        print(new_page.title())

        await asyncio.sleep(10)
        # 关闭浏览器
        await context.close()
        await browser.close()


def test_main():
    asyncio.run(main())


def test_main2():
    asyncio.run(main2())
