#!/usr/bin/env python3

import random
import asyncio
from aiohttp import ClientSession, ClientError
from aiohttp.http_exceptions import HttpProcessingError

from links_parser import LinksParser

seen = set()

async def print_url(url: str):
  await asyncio.sleep(random.randint(0, 3))
  print('printUrl: url=', url)

async def readerOld(url, session):
  #async with session.get(url) as response:
    #return await response.read(), response.headers
  response = await session.request(method="GET", url=url)
  response.raise_for_status()
  print("reader: fot response [%s] for URL: %s" % (response.status, url))
  html = await response.text()

  # you now have all response bodies in this variable
  # html = response[0].decode("utf-8")
  # html = response[0].decode("utf-8")
  # print("fetch: html = ", html)
  # print("fetch: header = ", response.headers)
  return html, response.headers

async def reader(url, session):
    async with session.get(url) as response:
      assert response.status == 200
      return await response.text(), response.headers

async def fetch(url):
  #url = "http://localhost:8080/1"
  # url = "http://docs.python.org"

  # Fetch all responses within one Client session,
  # keep connection alive for all requests.
  print("fetch: url =", url)
  retries = 1
  while True:
    try:
      async with ClientSession() as session:
        response = await reader(url, session)

        # response = await session.request(method="GET", url=url)
        # response.raise_for_status()
        # print("fetch: fot response [%s] for URL: %s" %(response.status, url))
        # html = await response.text()

        # you now have all response bodies in this variable
        #html = response[0].decode("utf-8")
        #html = response[0].decode("utf-8")
        #print("fetch: html = ", html)
        #print("fetch: header = ", response.headers)
        html = response[0]
        ct = response[1]['content-type']
        print("fetch:", response[1]['content-type'])
        if 'text/html' in ct or 'text/plain' in ct:
          links = LinksParser(url, seen).parse(html)
          #print('run: links=', links)
          #print('fetch: found text/plan or text/html')
          #print('run: html =\n', html)
          return links

        #print(response[0])
        return []
    except (ClientError, HttpProcessingError) as e:
      print("fetch: ERROR(%s) %s [%s]: %s" % (retries, url, getattr(e, "status", None), getattr(e, "message", None)))
      print("fetch: ERROR(%s) e = %s" % (retries, e))
      retries += 1
      if retries > 3:
        return []
    except Exception as e:
      print("fetch: non-aiohttp exception occurred:  %s" % e)


def fetch_done(future):
  print("fetch_done: got result:", future.result())
  async def run_caller():
    print("fetch_caller: got to call to run:", future.result())
    await run(future.result())
  asyncio.create_task(run_caller())


async def run(urls):
  print("run: called with urls =", urls)
  for url in urls:
    if url in seen:
      print("run: already seen url =", url)
      continue

    print('run: url =', url)
    links = await asyncio.ensure_future(fetch(url))
    print('run: links =', links)

    #tasks = [asyncio.create_task(fetch(link)) for link in links]

    tasks = []
    for link in links:
      print('run: got link', link);
      print('run: got link', link);

      task = asyncio.create_task(fetch(link))
      task.add_done_callback(fetch_done)
      tasks.append(task)
      # break;

    print("run: len(tasks)=", len(tasks))
    await asyncio.gather(*tasks);

    # tasks = []
    # print("run: got link", links[0]);
    # print("run: got link", links[1]);
    #
    # task = asyncio.create_task(fetch(links[0]))
    # task.add_done_callback(fetch_done)
    # tasks.append(task)
    #
    # task = asyncio.create_task(fetch(links[1]))
    # task.add_done_callback(fetch_done)
    # tasks.append(task)
    #
    # await asyncio.gather(*tasks);

  # tasks.append())
  # tasks.append(asyncio.create_task(fetch(links[1])))
  # more = await asyncio.gather(*tasks)
  # for url in more:
  #   print("run: more url:", url)

  # tasks = []
  # print("run: got link", links[1]);
  # tasks.append(asyncio.create_task(fetch(links[1])))
  # await asyncio.gather(*tasks)

def print_responses(result):
  print(result)

def main():
  loop = asyncio.get_event_loop()
  #future = asyncio.ensure_future(run("http://docs.python.org"))
  #loop.run_until_complete(run(["http://docs.python.org"]))
  #loop.run_until_complete(run(["https://docs.python.org/3/tutorial/index.html"]))
  loop.run_until_complete(run(["https://docs.python.org/3/tutorial/interpreter.html#the-interpreter-and-its-environment"]))

if __name__ == "__main__":
    main()