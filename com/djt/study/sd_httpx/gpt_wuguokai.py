"""
基于wuguokai的GPT接口
"""
import asyncio

import fake_useragent
import httpx

url = 'https://chat2.wuguokai.cn/api/chat-process'
ua = fake_useragent.UserAgent()
headers = {
    'User-Agent': ua.random,
    'origin': 'https://ai.wuguokai.cn',
    'referer': 'https://ai.wuguokai.cn'
}
timeout = httpx.Timeout(60)


async def ask(client: httpx.AsyncClient(), user_id, text: str):
    """
    提问
    :param client: http客户端
    :param user_id: 会话ID
    :param text: 提问内容
    :return: 回答
    """
    data = {
        "prompt": text,
        "userId": f"#/chat/{user_id}",
        "usingContext": True,
        "options": {}
    }
    headers['User-Agent'] = ua.random
    resp = await client.post(url=url, headers=headers, json=data, timeout=timeout)
    return resp.text


async def run():
    user_a = '1688550217237'
    user_b = '1688549698500'
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
