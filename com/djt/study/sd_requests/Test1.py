import json

import requests


def get_offline_rule():
    """
    获取离线分析规则
    :return:
    """
    url = 'http://172.20.6.6:37005/rule/getOfflineRule'
    body = {
        "ruleType": "06"
    }
    response = requests.post(url=url, json=body)
    print_response(response)


def get_statistics_rule():
    """
    获取实时统计规则
    :return:
    """
    url = 'http://172.20.6.6:37005/rule/getStatisticsRule'
    response = requests.post(url=url)
    print_response(response)


def print_response(response):
    """
    打印请求相应结果
    :param response:
    :return:
    """
    print(response.status_code)
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))


if __name__ == '__main__':
    # get_offline_rule()
    get_statistics_rule()
