# -*- encoding=utf8 -*-
__author__ = 'duanjiatao'
"""
蚂蚁森林
"""

import logging

from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

logger = logging.getLogger("airtest")
logger.setLevel(logging.WARN)

if not cli_setup():
    auto_setup(__file__, logdir=True,
               devices=['android://127.0.0.1:5037/10.150.190.17:5555?cap_method=MINICAP&touch_method=MAXTOUCH&', ],
               project_root=r'D:\workspace\Idea\IdeaProjects\study-python\com\djt\study\sd_airtest')

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 屏幕分辨率
resolution = (1080, 2400)


def start_alipay():
    """
    启动支付宝 并进入蚂蚁森林
    :return:
    """
    # 返回桌面
    home()
    # 启动APP
    start_app('com.eg.android.AlipayGphone')
    # sleep(1)
    go_alipay_home()
    # sleep(1)
    touch(Template(rf'.\image\ant_forest.png', resolution=resolution))
    sleep(2)


def go_alipay_home():
    """
    进入支付宝首页首页
    :return:
    """
    home = poco(text='扫一扫')
    while not home.exists():
        keyevent("BACK")
        sleep(0.5)


def steal_energy():
    """
    偷取能量
    :return:
    """
    # 找能量按钮
    find = Template(rf'.\image\find_energy.png', threshold=0.9, resolution=resolution)  # rgb=True,
    # 收能量按钮
    harvest = Template(rf'.\image\harvest_energy.png', threshold=0.9, resolution=resolution)
    # 循环找能量并收取
    while exists(find):
        while exists(harvest):
            touch(harvest)
            print('收取能量')
            sleep(0.5)
        touch(find)
        print('下一位')
        sleep(1)
    print('能量已收完')
    poco("android.widget.Button").click()


pass

if __name__ == '__main__':
    start_alipay()
    steal_energy()
