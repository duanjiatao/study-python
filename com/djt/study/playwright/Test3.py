import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, channel="msedge")
        context = await browser.new_context()
        page = await context.new_page()
        # await page.pause()
        await page.goto("https://qy.163.com/login/")
        for f in page.frames:
            print(f)

        await page.locator('//*[@id="switchNormalCtrl"]').click()
        await page.locator("#accname").fill("duanjiatao@xgd.com")
        await page.locator("#accpwd").fill("xxxxxx")
        await page.locator("form[name=\"accountlogin\"] div").filter(has_text="我已阅读并同意 服务条款 和 隐私政策").locator(
            "span").first.click()
        await page.get_by_role("button", name="登 录").click()
        await page.get_by_role("link", name="获取验证码").click()

        await asyncio.sleep(10)
        # 关闭浏览器
        await context.close()
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
