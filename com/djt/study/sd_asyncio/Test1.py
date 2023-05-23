import asyncio
import time


async def do_a():
    print("A is doing...")
    await asyncio.sleep(5)
    print("A is done")


async def do_b():
    print("B is doing...")
    await asyncio.sleep(5)
    print("B is done")


async def do_c():
    print("C is doing...")
    await asyncio.sleep(5)
    print("C is done")


async def do():
    tasks = [asyncio.create_task(do_a()), asyncio.create_task(do_b()), asyncio.create_task(do_c())]
    done, pending = await asyncio.wait(tasks)
    results = [task.result() for task in done]
    print(f"All tasks finished. Results: {results}")


start = time.perf_counter()
asyncio.run(do())
end = time.perf_counter()
print(f"总耗时:{end - start}")

asyncio.gather()
