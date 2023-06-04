import asyncio

from playwright.async_api import async_playwright, Page

edge_data_dir = r'D:\tmp\playwright\edge'
phone_no = '15091153321'


async def main():
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(headless=False, channel='msedge',
                                                             user_data_dir=edge_data_dir)
        page = await context.new_page()
        tt = TouTiao(page)
        await tt.run()

        await asyncio.sleep(30)
        await context.close()


class TouTiao:
    home_url = 'https://www.toutiao.com/'

    def __init__(self, page: Page):
        self.__page = page

    async def run(self):
        await self.__page.goto(self.home_url, wait_until='domcontentloaded', timeout=60000)
        print(self.__page.url)
        # 检测是否登录
        class_name = await self.__page.locator('//*[@id="root"]/div/div[5]/div[2]/div[1]/div/a').get_attribute('class')
        # 未登录
        if class_name == 'login-button':
            print('未登录！')
            await self.login()
        else:
            print('已登录')

    async def login(self):
        """
        登录
        :return:
        """
        # 点击登录按钮
        await asyncio.sleep(3)
        await self.__page.click('//*[@id="root"]/div/div[5]/div[2]/div[1]/div/a')
        # 输入手机号
        await self.__page.type(
            '//*[@id="login_modal_ele"]/div/article/article/div[1]/div[1]/div[2]/article/div[1]/div/input',
            text=phone_no, delay=200)
        # 发送验证码
        await self.__page.click(
            '//*[@id="login_modal_ele"]/div/article/article/div[1]/div[1]/div[2]/article/div[2]/div/span')
        check_code = input('请输入验证码:')
        # 填充验证码
        await self.__page.type(
            '//*[@id="login_modal_ele"]/div/article/article/div[1]/div[1]/div[2]/article/div[2]/div/div/input',
            text=check_code, delay=200)
        # 检查是否勾选协议
        is_check = await self.__page.locator(
            '//*[@id="login_modal_ele"]/div/article/article/div[1]/div[1]/div[2]/article/div[4]/span[1]') \
            .get_attribute('aria-checked')
        if is_check == 'false':
            await self.__page.get_by_role("checkbox", name="协议勾选框").click()
        # 等待登录按钮可点击
        bt_login = await self.__page.wait_for_selector(
            '//*[@id="login_modal_ele"]/div/article/article/div[1]/div[1]/div[2]/article/div[5]/button',
            state='visible', timeout=60)
        while not await bt_login.is_enabled():
            await asyncio.sleep(1)
        # 点击登录按钮
        await bt_login.click()
        print('登录成功')


if __name__ == '__main__':
    asyncio.run(main())
