import json
import aiohttp
import asyncio
import async_timeout

async def read_text(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            assert response.status == 200
            return await response.text()

async def read_data(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            assert response.status == 200
            return await response.read()

async def main():
    async with aiohttp.ClientSession() as session:
        # read response as text
        html = await read_text(session, "http://www.python.org")
        print(html)

        # read response as binary with decode
        html = await read_data(session, "http://www.python.org")
        html = html.decode('utf-8')
        print(html)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



