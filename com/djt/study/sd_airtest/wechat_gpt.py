# -*- encoding=utf8 -*-
__author__ = 'duanjiatao'
"""
airtest监控微信聊天，并使用GPT与对方聊天

"""

import logging
import traceback

from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from com.djt.study.sd_httpx.gpt_jinshutuan import ask_async

logger = logging.getLogger("airtest")
logger.setLevel(logging.WARN)

if not cli_setup():
    auto_setup(__file__, logdir=True,
               devices=['android://127.0.0.1:5037/10.150.190.17:5555?cap_method=MINICAP&touch_method=MAXTOUCH&', ],
               project_root=r'D:\workspace\Idea\IdeaProjects\study-python\com\djt\study\sd_airtest')

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 账号名
my_name = '涛哥二号'
# 头像名
my_logo = my_name + '头像'
# 微信图标(存在双开)
wechat = 'wechat2'
# 对话超时时间
chat_timeout = 60
# GPT回话ID
chat_user_id = '1689045263535'
# 每个对话的最后一条消息
chat_last_msg = {}


def start_wx():
    """
    启动微信
    :return:
    """
    # 唤醒屏幕
    wake()
    # 返回桌面
    home()
    # 启动微信
    touch(Template(rf'.\image\{wechat}.png', resolution=(1080, 2400)))


def go_chat_home():
    """
    进入聊天首页
    :return:
    """
    chat_home = poco(text='微信')
    while not chat_home.exists():
        keyevent("BACK")
        sleep(1)
    chat_home.click()


def start_listen():
    """
    启动消息监听
    :return:
    """
    print('启动消息监听...')
    while True:
        # 返回聊天首页
        go_chat_home()
        # 检查是否有未读消息
        unread_msg = poco('com.tencent.mm:id/kmv')
        if not unread_msg.exists():
            sleep(1)
            continue
        unread_msg.click()
        poco('com.tencent.mm:id/eo').click()
        title = poco('android:id/title')
        is_group = False
        if title.exists() and title.get_text() == '群聊名称':
            is_group = True
        poco('com.tencent.mm:id/g1').click()
        handle_chat(is_group)


def handle_chat(is_group=False):
    """
    处理一个对话框
    最后一条对方的消息发生变化，则可认为收到了新消息
    五秒之内无新消息，则返回聊天主页
    :param is_group:是否是群聊
    :return:
    """
    # 对方名称
    name = poco('com.tencent.mm:id/ko4').get_text()
    print(f'进入[{name}]对话框...')
    # 计时器
    start = time.perf_counter()
    while True:
        msg = get_last_msg(is_group)
        # 没有新消息
        if msg is None or msg == chat_last_msg.get(name):
            if (time.perf_counter() - start) >= chat_timeout:
                print(f'[{name}]长时间无消息，已退出聊天！')
                return
            else:
                # sleep(1)
                continue
        # 新消息处理 发送给GPT获取回答 并将答案发送给对方
        print(f'[{name}]提问=>{msg}')
        answer = ask_async(chat_user_id, msg)
        print(f'[GPT]回答=>{answer}')
        poco("com.tencent.mm:id/kii").click()
        text(answer, enter=False)
        sleep(0.2)
        poco('com.tencent.mm:id/b8k').click()
        # 更新最后一条消息
        chat_last_msg[name] = msg
        start = time.perf_counter()
        # sleep(1)


def get_last_msg(is_group=False):
    """
    获取当前对话框最后一条消息
    :param is_group:是否是群聊
    :return:
    """
    hp_list = poco('com.tencent.mm:id/hp')
    if not hp_list.exists():
        return None
    for i in range(0, len(list(hp_list))):
        last_hp = hp_list[-1 * (i + 1)]
        if not last_hp.exists():
            continue
        # 头像
        b3s = last_hp.offspring('com.tencent.mm:id/b3s')
        # 聊天内容
        b4b = last_hp.offspring('com.tencent.mm:id/b4b')
        if b3s is not None and b3s.exists() and b4b is not None and b4b.exists() and \
                b4b.attr('type') == 'android.widget.TextView' and b3s.attr('desc') != my_logo:
            msg = b4b.get_text()
            if not is_group:
                return msg
            elif msg.startswith(f'@{my_name}'):
                return msg.replace(f'@{my_name}', '').strip()
    return None


def get_question_list():
    """
    获取当前对话框待回答的问题列表
    :return:
    """
    hp_list = poco('com.tencent.mm:id/hp')
    if not hp_list.exists():
        return None
    # 待实现...


if __name__ == '__main__':
    try:
        start_wx()
        print('微信已启动...')
        # 切换输入法
        device().yosemite_ime.start()
        print('输入法已切换...')
        start_listen()
    except Exception as e:
        traceback.print_exc()
    finally:
        # 换回输入法
        device().yosemite_ime.end()
