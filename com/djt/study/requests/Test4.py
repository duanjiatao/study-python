import requests

from com.djt.study.requests.Test3 import check_ip

"""
测试自建代理IP池
"""

pool_url = 'http://172.20.7.41:60039'  # http://172.20.7.41:60039  http://demo.spiderpy.cn/


def get_proxy():
    """
    从搭建的IP池获取代理IP
    :return:
    """
    return requests.get(f"{pool_url}/get/").json()


def delete_proxy(proxy):
    """
    删除IP池中的IP
    :param proxy:
    :return:
    """
    requests.get(f"{pool_url}/delete/?proxy={proxy}")


def test_pool():
    for _ in range(100):
        proxy = get_proxy()
        ip = proxy.get('proxy')
        if not check_ip(ip):
            delete_proxy(ip)
