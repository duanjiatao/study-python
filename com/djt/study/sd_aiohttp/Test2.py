import asyncio
import time

import aiohttp
import requests

"""
requests 与 aiohttp 对比测试
"""

url = 'https://www.baidu.com'
count = 100


def request():
    for _ in range(count):
        resp = requests.get(url)
        print(resp.status_code)


async def aiohttp1():
    async with aiohttp.ClientSession() as session:
        for _ in range(count):
            async with session.get(url) as resp:
                print(resp.status)


async def get_pokemon(session):
    async with session.get(url) as resp:
        print(resp.status)


async def aiohttp2():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(count):
            tasks.append(asyncio.create_task(get_pokemon(session)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    start_time = time.perf_counter()
    request()
    cost1 = time.perf_counter() - start_time

    start_time = time.perf_counter()
    loop.run_until_complete(aiohttp1())
    cost2 = time.perf_counter() - start_time

    start_time = time.perf_counter()
    loop.run_until_complete(aiohttp2())
    cost3 = time.perf_counter() - start_time

    print(f"--- requests 耗时：{cost1} ---")
    print(f"--- aiohttp1 耗时：{cost2} ---")
    print(f"--- aiohttp2 耗时：{cost3} ---")
