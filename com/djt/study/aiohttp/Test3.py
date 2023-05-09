import asyncio

import aiohttp


async def post_v1():
    data = {'key': 'value'}  # 传递form表单
    async with aiohttp.ClientSession() as sess:
        async with sess.post('http://httpbin.org/post', data=data) as resp:
            print(resp.status)


# 复杂的 post 请求
async def post_v2():
    payload = {'key': 'value'}  # 传递 pyload
    async with aiohttp.ClientSession() as sess:
        async with sess.post('http://httpbin.org/post', json=payload) as resp:
            print(resp.status)


if __name__ == '__main__':
    asyncio.run(post_v1())
    asyncio.run(post_v2())
