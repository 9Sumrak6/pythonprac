import asyncio

'''
Do not work
'''


async def squarer(x):
    return x ** 2

async def doubler(x):
    return 2 * x

async def main():
    res = await asyncio.gather(
        squarer(float(input())),
        squarer(float(input()))
    )
    res = await asyncio.gather(
        doubler(res[0]),
        doubler(res[1])
    )
    print(res)
    return res

asyncio.run(main())
