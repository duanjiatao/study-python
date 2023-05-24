import asyncio
from asyncio.queues import Queue


async def tt_queue():
    queue = Queue()
    for i in range(10):
        await queue.put(i)

    for _ in range(queue.qsize()):
        print(await queue.get())


def test1():
    asyncio.run(tt_queue())
