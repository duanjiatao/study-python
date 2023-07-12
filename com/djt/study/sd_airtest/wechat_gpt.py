# -*- encoding=utf8 -*-
__author__ = 'duanjiatao'
"""
airtest监控微信聊天，并使用GPT与对方聊天

"""

from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.proxy import UIObjectProxy

from com.djt.study.sd_httpx.gpt_jinshutuan import ask_async

if not cli_setup():
    auto_setup(__file__, logdir=True,
               devices=['android://127.0.0.1:5037/10.150.190.17:5555?cap_method=MINICAP&touch_method=MAXTOUCH&', ],
               project_root=r'D:\workspace\Idea\IdeaProjects\study-python\com\djt\study\sd_airtest')

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 　'涛哥二号'  '　'
my_name = '涛哥二号'
my_logo = my_name + '头像'
wechat = 'wechat2'
chat_timeout = 24 * 3600
chat_user_id = '1689045263535'
print('start...')


def start_wx():
    """
    启动微信 并返回聊天主页
    :return:
    """
    # 唤醒屏幕
    wake()
    # 返回桌面
    home()
    # 启动微信
    touch(Template(rf'.\image\{wechat}.png', resolution=(1080, 2400)))
    # 进入聊天首页
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
    while True:
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
    # 返回按钮
    bt_back = poco('com.tencent.mm:id/yn')
    # 计时器
    start = time.perf_counter()
    # 最后一条消息
    last_msg = None
    while True:
        hp_list = poco('com.tencent.mm:id/hp')
        if not hp_list.exists():
            bt_back.click()
            return
        msg = get_last_msg(hp_list, is_group)
        # 没有新消息
        if msg is None or msg == last_msg:
            if (time.perf_counter() - start) >= chat_timeout:
                bt_back.click()
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
        last_msg = msg
        start = time.perf_counter()
        # sleep(1)


def get_last_msg(hp_list: UIObjectProxy, is_group=False):
    """
    获取当前对话框最后一条消息
    :param hp_list:消息列表
    :param is_group:是否是群聊
    :return:
    """
    for i in range(1, len(list(hp_list))):
        last_hp = hp_list[-1 * i]
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


if __name__ == '__main__':
    try:
        start_wx()
        # 切换输入法
        device().yosemite_ime.start()
        start_listen()
    except Exception as e:
        print(e)
    finally:
        # 换回输入法
        device().yosemite_ime.end()

# if __name__ == '__main__':
#     try:
#         # start_wx()
#         # # 切换输入法
#         device().yosemite_ime.start()
#         # poco('com.tencent.mm:id/hg4').click()
#         # msg_list = poco('com.tencent.mm:id/hp')
#         # print(f'最后一条消息=>{get_last_msg(msg_list, is_group=True)}')
#         handle_chat(is_group=True)
#     finally:
#         # 换回输入法
#         device().yosemite_ime.end()
