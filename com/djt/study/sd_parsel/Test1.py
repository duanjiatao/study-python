"""
测试异步 httpx + parsel
"""

import asyncio
import time
from asyncio.queues import Queue

import fake_useragent
import httpx
import parsel

from com.djt.study.sd_requests.Test6 import MovieInfo

ua = fake_useragent.UserAgent()
headers = {
    'User-Agent': ua.random
}


async def get_douban(url: str, client: httpx.AsyncClient, queue: Queue) -> None:
    """
    爬取豆瓣电影top250
    :param url: 链接
    :param client: http客户端(异步)
    :param queue: 结果队列
    :return:
    """
    resp = await client.get(url=url, headers=headers)
    if resp.status_code != 200:
        raise Exception("请求异常:", resp.text)
    selector = parsel.Selector(resp.text)
    li_list = selector.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for li in li_list:
        movie = parse_moive_info(li)
        await queue.put(movie)


def parse_moive_info(selector: parsel.Selector) -> MovieInfo:
    """
    将标签内容转换为对象
    :param selector:
    :return:
    """
    order = selector.xpath('.//div[1]/em/text()').get()
    name = selector.xpath('.//div[2]/div[1]/a/span[1]/text()').get()
    score = selector.xpath('.//div[2]/div[2]/div/span[2]/text()').get()
    summ_info = selector.xpath('.//div[2]/div[2]/p[1]/text()[1]').get().strip() + ' ' * 3 + \
                selector.xpath('.//div[2]/div[2]/p[1]/text()[2]').get().strip()
    p_num = selector.xpath('.//div[2]/div[2]/div/span[4]/text()').get()
    href = selector.xpath('.//div[2]/div[1]/a/@href').get()
    return MovieInfo(order, name, score, summ_info, p_num, href)


async def run():
    """
    分页爬取
    :return:
    """
    queue = Queue()
    tasks = []
    async with httpx.AsyncClient() as client:
        for i in range(10):
            url = f'https://movie.douban.com/top250?start={i * 25}'
            tasks.append(get_douban(url, client, queue))
        # 注意: 该代码必须在with代码块内，否则client会自动关闭，导致运行报错
        await asyncio.wait(tasks)
    # 遍历打印
    for _ in range(queue.qsize()):
        print(await queue.get())
        print('=' * 100)


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(run())
    print(f'总耗时:{time.perf_counter() - start}')
