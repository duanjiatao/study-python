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


if __name__ == '__main__':
    asyncio.run(main())
