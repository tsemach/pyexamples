import asyncio
import datetime
import random

"""
from: http://masnun.com/2015/11/13/python-generators-coroutines-native-coroutines-and-async-await.html

If we see the output, we shall see that the two coroutines are executed concurrently. 
When we use yield from, the event loop knows that it’s going to be busy 
for a while so it pauses execution of the coroutine and runs another. 
Thus two coroutines run concurrently (but not in parallel since the event loop is single threaded).
"""

async def display_date(num, loop, ):
    end_time = loop.time() + 20.0
    while True:
        print("loop.time() = {} end_time = {}".format(loop.time(), end_time))
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(random.randint(0, 5))
    print("End of loop %s" % num)


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()