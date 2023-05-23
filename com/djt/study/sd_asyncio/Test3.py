import asyncio

"""
信号量 Semaphore 测试
注意：全局的Semaphore变量在使用asyncio.run时会报错，此时有以下几种解决办法
1.使用asyncio.get_event_loop().run_until_complete
2.在main中创建Semaphore，并将其作为参数传递至协程中
3.使用global关键字声明Semaphore(不推荐)
"""


async def worker(sem, idx):
    async with sem:
        print(f"{idx} Acquired lock")
        await asyncio.sleep(3)
        print(f"{idx} Released lock")


async def main():
    sem = asyncio.Semaphore(5)
    tasks = [asyncio.ensure_future(worker(sem, i)) for i in range(10)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
