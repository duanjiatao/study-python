import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
}


def check_proxy():
    """
    免费代理IP提取并验证可用性
    :return:
    """
    # ip_list = get_ip_from_html()
    ip_list = get_ip_from_html2()
    for ip in ip_list:
        check_ip(ip)


def check_ip(ip):
    """
    检查IP是否可用
    :param ip:
    :return:
    """
    check_url = 'http://www.example.com/'
    proxies = {'http': f'http://{ip}', 'https': f'https://{ip}'}
    try:
        response = requests.get(url=check_url, headers=headers, proxies=proxies, timeout=5)
        if response.status_code == 200:
            print(ip)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def get_ip_from_html():
    # url = 'https://www.kuaidaili.com/free/inha/'  # 国内高匿代理
    url = 'https://www.kuaidaili.com/free/intr/'  # 国内普通代理
    response = requests.get(url=url, headers=headers)
    html = response.text.encode(response.encoding)
    soup = BeautifulSoup(html, features='lxml')
    rows = soup.select('#list > table > tbody > tr')
    ip_list = []
    for row in rows:
        # print('=' * 50)
        # print(row)
        ip = row.select('[data-title="IP"]')[0].text
        port = row.select('[data-title="PORT"]')[0].text
        ip_port = f'{ip}:{port}'
        print(ip_port)
        ip_list.append(ip_port)
    print('=' * 100)
    return ip_list


def get_ip_from_html2():
    # url = 'http://www.kxdaili.com/dailiip/2/1.html'  # 国内普通代理
    url = 'http://www.kxdaili.com/dailiip/1/1.html'  # 国内高匿代理
    response = requests.get(url=url, headers=headers)
    html = response.text.encode(response.encoding)
    soup = BeautifulSoup(html, features='lxml')
    rows = soup.select(
        'body > div > div.header-container > div.domain-block.price-block > div.auto > div.hot-product > div.hot-product-content > table > tbody > tr')
    ip_list = []
    for row in rows:
        # print('=' * 50)
        # print(row)
        tds = row.select('td')
        ip_port = f'{tds[0].text}:{tds[1].text}'
        print(ip_port)
        ip_list.append(ip_port)
    print('=' * 100)
    return ip_list


def get_proxy():
    """
    从搭建的IP池获取代理IP
    :return:
    """
    return requests.get("http://172.20.7.41:60039/get/").json()


def delete_proxy(proxy):
    """
    删除IP池中的IP
    :param proxy:
    :return:
    """
    requests.get("http://172.20.7.41:60039/delete/?proxy={}".format(proxy))


def tt_pool():
    for _ in range(100):
        proxy = get_proxy()
        ip = proxy.get('proxy')
        if not check_ip(ip):
            delete_proxy(ip)


if __name__ == '__main__':
    # check_proxy()
    # check_ip('58.57.170.154:9002')
    # get_ip_from_html()
    # get_ip_from_html2()
    tt_pool()
