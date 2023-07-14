# -*- encoding=utf8 -*-
__author__ = 'duanjiatao'

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

swipe((900, 200), (100, 200))
print("滑动完成")
sleep(3)
