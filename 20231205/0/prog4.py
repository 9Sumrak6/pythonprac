import asyncio

async def prod(q):
    for i in range(5):
        await q.put(f"value_{i}")
        print(f"prod value_{i}")
        await asyncio.sleep(1)
    await q.put(None)

async def mid(q1, q2):
    while True:
        res = await q1.get()
        print(f"mid {res}")
        await q2.put(res)
        if res == None:
            break

async def cons(q2):
    while True:
        res = await q2.get()
        if res == None:
            break
        print(f"cons {res}")

async def main():
    q1, q2 = asyncio.Queue(), asyncio.Queue()
    res = await asyncio.gather(
            prod(q1),
            mid(q1, q2),
            cons(q2)
            )

asyncio.run(main())
