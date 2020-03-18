#!/usr/bin/env python3

import asyncio

async def count_fast():
    print("count_fast(): one")
    await asyncio.sleep(1)
    print("count_fast(): two")

async def count_slow():
    print("count_slow(): one")
    await asyncio.sleep(3)
    print("count_slow(): two")

async def main():
    await asyncio.gather(count_slow(), count_fast())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print("{__file__} executed in {elapsed:0.2f} seconds.")