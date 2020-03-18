#!/usr/bin/env python3

import asyncio
from aiohttp import ClientSession

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read(), response.headers

async def run_gather():
    url = "http://localhost:8080/1"
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        task = asyncio.ensure_future(fetch(url, session))
        tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        print(responses[0][0])
        print(responses[0][1])

def print_responses(result):
    print(result)

def main():
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run_gather())
    loop.run_until_complete(future)

if __name__ == "__main__":
    main()