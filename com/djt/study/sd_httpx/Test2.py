"""
实现两个机器人对话
"""

import asyncio

import fake_useragent
import httpx

url = 'https://api.binjie.fun/api/generateStream'
ua = fake_useragent.UserAgent()
headers = {
    'User-Agent': ua.random,
    'origin': 'https://chat.jinshutuan.com',
    'referer': 'https://chat.jinshutuan.com'
}
timeout = httpx.Timeout(60)


async def ask(client: httpx.AsyncClient(), user_id, text: str):
    data = {
        "prompt": text,
        "userId": f"#/chat/{user_id}",
        "network": True,
        "system": "",
        "withoutContext": False,
        "stream": False
    }
    headers['User-Agent'] = ua.random
    resp = await client.post(url=url, headers=headers, data=data, timeout=timeout)
    return resp.text


async def run():
    user_a = '1685093567531'
    user_b = '1685093564530'
    async with httpx.AsyncClient() as client:
        text = '你好'
        while True:
            text = await ask(client, user_a, text)
            print(f'A=>{text}')
            print('=' * 100)
            text = await ask(client, user_b, text)
            print(f'B=>{text}')
            print('=' * 100)
            await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(run())
