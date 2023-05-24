import os
import time

from playwright.sync_api import sync_playwright


def test_login():
    """
    测试保存登录信息
    :return:
    """
    print()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel='msedge', args=["--start-maximized"])  # 窗口最大化
        context = browser.new_context(no_viewport=True)  # 指定窗口大小传参： viewport={'width': 1920, 'height': 1080}
        page = context.new_page()
        # 访问网址
        page.goto('https://manage-dev.jlpay.com/login')
        # 输入账号密码
        page.get_by_placeholder("请输入账号").fill("duanjiatao")
        page.locator("#SIPBox4").click()
        page.type("#SIPBox4", "djt0123456", delay=100)
        # 点击登录按钮 等待页面跳转
        with page.expect_navigation():
            page.get_by_role("button", name="登录").click()

        page.wait_for_load_state()
        print("#" * 10, page.url)
        # 点击管理系统图标 等待打开页面
        with page.expect_popup() as mng_page_info:
            page.click('//*[@id="app"]/div/div[1]/main/div[1]/div[2]/div[2]/div')
        mng_page = mng_page_info.value
        mng_page.wait_for_load_state()
        print("#" * 10, mng_page.url)
        # 等待加载至最终页面
        mng_page.wait_for_load_state(state='networkidle')
        print("#" * 10, mng_page.url)

        # page.pause()
        context.storage_state(path='auth/mng.json')
        time.sleep(5)
        context.close()
        browser.close()


def test_longin2():
    """
    测试是否需要重复登录
    :return:
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel='msedge')
        context = browser.new_context(storage_state='auth/mng.json')
        page = context.new_page()
        page.goto(
            'https://mng-dev.jlpay.com/system/views/index.html?params=%7B%22access_token%22%3A%22eyJ0eXAiOiJKV1QiLCJwbGF0IjoiQUMiLCJhbGciOiJTTTNXaXRoU00yIn0.eyJzdWIiOiJQIiwidWlkIjoiMjAyMDAyMTc4MDA0MTY0OCIsIm5iZiI6MTY4NDM4ODI3MiwidW5hbWUiOiLmrrXkvbPmtpsiLCJpc3MiOiJKTFBBWSIsImV4cCI6MTY4NDQ3NDY3MiwiaWF0IjoxNjg0Mzg4MjcyLCJqdGkiOiIyMTMzMjUwNjQ4NzIyNzIxMXQwbkp1RTd5TncifQ.MEQCIAnJkBk3uQESu-Jq5r68tY19TKiQsgm5Mu64oYtA-icWAiB8cZubFvB1_u0dOQ7ZI7jKWJu04FQOdNgNDYsjPzlm1w%22%2C%22user_id%22%3A%222020021780041648%22%2C%22user_name%22%3A%22%E6%AE%B5%E4%BD%B3%E6%B6%9B%22%2C%22mobile%22%3A%22150****3321%22%2C%22lastLoginTime%22%3A%222023-05-18%2011%3A45%3A59%22%2C%22plat_code%22%3A%22manage%22%2C%22web_name%22%3A%22https%3A%2F%2Fmanage-dev.jlpay.com%22%7D')

        time.sleep(5)
        context.close()
        browser.close()


def test_longin_github() -> None:
    """
    测试登录github
    检测是否有可用的cookies 若无则用账号密码登录 并保存cookies
    若有则尝试登陆 若cookies失效 则重新用账号密码登录并更新cookies
    :return:
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel='msedge')
        state_path = 'auth/github.json'
        if not os.path.exists(state_path):
            # 如果文件不存在，则创建一个空文件
            with open(state_path, 'w') as f:
                f.write('{"cookies":[],"origins":[]}')

        context = browser.new_context(storage_state=state_path)
        page = context.new_page()
        page.goto('https://github.com')
        # 等待页面加载完成至网络空闲状态
        page.wait_for_load_state('networkidle')
        # 如果未登录 则进行登录
        if page.query_selector(
                'body > div.logged-out.env-production.page-responsive.header-overlay.home-campaign > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu--logged-out.p-responsive.height-fit.position-lg-relative.d-lg-flex.flex-column.flex-auto.pt-7.pb-4.top-0 > div > div > div.position-relative.mr-lg-3.d-lg-inline-block > a'):
            login_github(page)

        print(page.url)
        # 保存当前页面的登录信息
        context.storage_state(path=state_path)

        time.sleep(5)
        context.close()
        browser.close()


def login_github(page):
    """
    登录github
    :param page:
    :return:
    """
    page.goto('https://github.com/login')
    page.get_by_label("Username or email address").fill("Username")
    page.get_by_label("Password").fill("Password")
    # 点击登录按钮 等待页面跳转至APP验证页面
    with page.expect_navigation():
        page.get_by_role("button", name="Sign in").click()
    # 输入APP验证码 等待自动跳转至首页
    page.wait_for_url(url='https://github.com/', wait_until="networkidle", timeout=60000)
