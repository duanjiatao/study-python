import asyncio
import random
import time

"""
测试多个task异步执行
"""


async def async_fun(name, sleep):
    print(f"{name} is going to run for {sleep} seconds.")
    await asyncio.sleep(sleep)
    print(f"{name} is done.")
    return name + str(sleep)


async def main():
    names = ["张三", "李四", "王五", "赵六", "侯七"]
    tasks = [asyncio.create_task(async_fun(name, random.randint(5, 10))) for name in names]
    # done, pending = await asyncio.wait(tasks)
    # results = [task.result() for task in done]
    # print(f"全部执行成功: {results}")
    results = await asyncio.gather(*tasks)
    print(f"全部执行成功: {results}")


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"总耗时:{end - start}")
