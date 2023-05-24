import asyncio
import time

import httpx


def test1():
    """
    httpx同步请求
    :return:
    """
    url = 'http://httpbin.org/get'
    resp = httpx.get(url=url)
    print(resp.text)


async def sync_get(url: str):
    """
    httpx同步客户端
    :return:
    """
    with httpx.Client() as client:
        resp = client.get(url=url)
        print(resp.text)


def test2():
    url = 'http://httpbin.org/get'
    sync_get(url)


async def async_get(url: str):
    """
    httpx异步客户端
    :return:
    """
    async with httpx.AsyncClient() as client:
        resp = await client.get(url=url)
        print(resp.text)


def test3():
    url = 'http://httpbin.org/get'
    asyncio.run(async_get(url))


def sync_post(url: str, data: dict) -> None:
    """
    同步post请求
    :param url:
    :param data:
    :return:
    """
    resp = httpx.post(url=url, data=data, timeout=10)
    print(resp.text)


async def async_post(url: str, data: dict) -> None:
    """
    异步post请求
    :param url:
    :param data:
    :return:
    """
    async with httpx.AsyncClient() as client:
        resp = await client.post(url=url, data=data, timeout=10)
        print(resp.text)


def test4():
    """
    连续同步请求测试
    :return:
    """
    url = 'http://httpbin.org/post'
    data = {}
    start = time.perf_counter()
    for i in range(10):
        data['num'] = i
        sync_post(url, data)
        print('=' * 50)
    print(f'总耗时:{time.perf_counter() - start}')


def test5():
    """
    连续异步请求测试
    :return:
    """
    url = 'http://httpbin.org/post'
    data = {}
    tasks = []
    start = time.perf_counter()
    for i in range(10):
        data['num'] = i
        tasks.append(async_post(url, data))
    # 执行所有异步任务
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print(f'总耗时:{time.perf_counter() - start}')
