import time

from playwright.sync_api import sync_playwright


def test_hover():
    """
    测试鼠标悬停
    :return:
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel="msedge")
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        dropdown = page.locator('.dropdown--hoverable')
        # 鼠标悬停
        dropdown.hover()
        # 点选项
        dropdown.locator('.dropdown__link >> text=python').click()
        time.sleep(5)
        browser.close()


def test_devies():
    """
    查看支持哪些设备
    :return:
    """
    with sync_playwright() as p:
        for device in p.devices:
            print(device)
