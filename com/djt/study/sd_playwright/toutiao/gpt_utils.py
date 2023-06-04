import asyncio
import time

import fake_useragent
import httpx

async_client = httpx.AsyncClient()
url = 'https://api.binjie.fun/api/generateStream'
ua = fake_useragent.UserAgent()
headers = {
    'User-Agent': ua.random,
    'origin': 'https://chat.jinshutuan.com',
    'referer': 'https://chat.jinshutuan.com'
}
timeout = httpx.Timeout(60)


async def gpt_ask(question: str) -> str:
    """
    提问GPT并获取回答
    :param question:问题
    :return:
    """
    data = {
        "prompt": question,
        "userId": f"#/chat/{int(time.time() * 1000)}",
        "network": True,
        "system": "",
        "withoutContext": False,
        "stream": False
    }
    headers['User-Agent'] = ua.random
    resp = await async_client.post(url=url, headers=headers, data=data, timeout=timeout)
    return resp.text


async def main():
    resp = await gpt_ask('今天几号')
    print(resp)


if __name__ == '__main__':
    asyncio.run(main())
