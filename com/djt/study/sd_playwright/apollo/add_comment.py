"""
给Apollo配置自动添加注释
"""
import time

from playwright.sync_api import sync_playwright

from com.djt.study.sd_pymysql.config import decrypt

# Apollo url
url = 'http://apollo-ui-pro.jlpay.io'

# 登录账号密码
user_name = 'duanjiatao'
password = 'd4ab4399179c4f31cc13436d3947fddab38d8d329be01dd988e2e6710e470b13'

# 项目列表
appid_arr = ['RISKCTRL.risk-stat-payorder', 'RISKCTRL.risk-stat-payment', 'RISKCTRL.risk-stat-archive']


def login(page):
    """
    登录Apollo
    """
    page.goto(url)
    page.fill('#login-form > div:nth-child(2) > input', user_name)
    page.fill('#login-form > div:nth-child(3) > input', decrypt(password))
    page.click('#login-submit')
    page.wait_for_load_state()
    print('登录成功')


def add_comment(page, appid, env, cluster='default'):
    """
    添加注释
    @param page: 页面
    @param appid: appid
    @param env: 环境
    @param cluster: 集群
    @return:
    """
    app_url = f'{url}/config.html?#/appid={appid}&env={env}&cluster={cluster}'
    print(f'开始为该项目添加注释: {app_url}')
    page.goto(app_url, timeout=5000, wait_until='networkidle')
    # 展开所有配置
    expand_all_namespace(page)
    time.sleep(1)
    # 获取所有配置
    config_lines = page.query_selector_all('tr[ng-repeat="config in namespace.viewItems |orderBy:col:desc"]')
    if not config_lines:
        print(f"当前环境未发现任何配置: {app_url}")
        return

    count = 0
    for line in config_lines:
        count += 1
        key = line.query_selector('span[ng-bind*="config.item.key"]').text_content()
        value = line.query_selector('span[ng-bind*="config.item.value"]').text_content()
        # edit = line.query_selector('img[src="img/edit.png"]')
        # edit.click()
        # 填充备注
        # page.fill(selector='//*[@id="itemModal"]/div/div/div[2]/div[3]/div/textarea', value='666')
        # 提交 注意：点击提交之后会自动刷新页面，因此该方法暂不适用！
        # page.click('//*[@id="itemModal"]/div/div/div[3]/button[2]')
        print(f'{count} {key}={value}')
        time.sleep(0.1)


def expand_all_namespace(page):
    """
    展开所有namespace(有的需要点击加载)
    @param page:
    @return:
    """
    # 未加载的namespace
    namespaces = page.query_selector_all('button:has-text("加载Namespace")')
    if namespaces:
        # 点击加载所有namespace
        for ns in namespaces:
            ns.click()
            time.sleep(0.1)
    else:
        # 已加载的namespace
        namespaces = page.query_selector_all('span[class^="label no-radius cursor-pointer"]')
        for ns in namespaces:
            ns.click()
            time.sleep(0.1)


def run():
    """
    执行入口
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel='msedge')
        context = browser.new_context()
        page = context.new_page()

        login(page)
        # add_comment(page, appid='RISKCTRL.risk-stat-payorder', env='DEV')
        add_comment(page, appid='xdata.xdata-commons', env='DEV')
        # add_comment(page, appid='XDATA.xdata-tag-manage', env='DEV')
        time.sleep(10)

        context.close()
        browser.close()


if __name__ == '__main__':
    run()
    print('完成')
