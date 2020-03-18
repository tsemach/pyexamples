#!/usr/bin/env python3

"""
from: https://realpython.com/async-io-python/#async-io-design-patterns
"""

import asyncio
import random
import time


async def part1(n: int) -> str:
  i = random.randint(0, 10)
  print("part1({}) sleeping for {} seconds.".format(n, i))
  await asyncio.sleep(i)
  result = "result1-{}".format(n)
  print("part1: return ({}) == {}".format(n, result))
  return result

async def part2(n: int, arg: str) -> str:
  print("part2: called n={}, arg={}".format(n, arg))
  i = random.randint(0, 10)
  print("part2: {} {} sleeping for {} seconds.".format(n, arg, i))
  await asyncio.sleep(i)
  result = "result{}-2 derived from {}".format(n, arg)
  print("part2: return {} {} == {}.".format(n, arg, result))
  return result

async def chain(n: int) -> None:
  print("chain({}): is called n={}".format(n, n))
  start = time.perf_counter()
  p1 = await part1(n)
  p2 = await part2(n, p1)
  end = time.perf_counter() - start
  #print("Chained: result {} => {} (took {0.2f} seconds).".format(n, p2, end))
  print("Chained: result {} => {} took {:0.2f}".format(n, p2, end))

async def main(*args):
  await asyncio.gather(*(chain(n) for n in args))

if __name__ == "__main__":
  import sys
  random.seed(444)
  args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
  start = time.perf_counter()
  asyncio.run(main(*args))
  end = time.perf_counter() - start
  print("Program finished in {:0.2f} seconds".format(end))