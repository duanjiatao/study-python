import time

from playwright.sync_api import sync_playwright


def test_download():
    """
    测试下载
    :return:
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel='msedge')
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://repo.huaweicloud.com/java/jdk/8u202-b08/')
        with page.expect_download() as download_info:
            page.locator('body > pre:nth-child(4) > a:nth-child(7)').click()
        download = download_info.value
        download.save_as(f'C:\\Users\\duanjiatao\\Desktop\\{download.suggested_filename}')
        time.sleep(5)
        context.close()
        browser.close()


def test_on():
    """
    事件监听
    :return:
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel='msedge')
        page = browser.new_page()
        # 监听请求和响应事件
        page.on("request", lambda request: print(">>", request.method, request.url))
        page.on("response", lambda response: print("<<", response.status, response.url))
        page.goto("https://cn.bing.com/")

        time.sleep(5)
        browser.close()
