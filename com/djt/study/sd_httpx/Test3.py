"""
实现两个机器人对话
"""

import asyncio

import httpx

import gpt_jinshutuan
import gpt_wuguokai


async def run():
    user_a = '1685093567531'
    user_b = '1685093564530'
    async with httpx.AsyncClient() as client:
        text = '你好'
        while True:
            text = await gpt_jinshutuan.ask(client, user_a, text)
            print(f'A=>{text}')
            print('=' * 100)
            text = await gpt_wuguokai.ask(client, user_b, text)
            print(f'B=>{text}')
            print('=' * 100)
            await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(run())
