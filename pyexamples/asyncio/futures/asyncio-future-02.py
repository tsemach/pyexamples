import asyncio
import time

"""
from: http://masnun.com/2015/11/13/python-generators-coroutines-native-coroutines-and-async-await.html

If we see the output, we shall see that the two coroutines are executed concurrently. 
When we use yield from, the event loop knows that it’s going to be busy 
for a while so it pauses execution of the coroutine and runs another. 
Thus two coroutines run concurrently (but not in parallel since the event loop is single threaded).
"""

async def myTask():
    time.sleep(1)
    print("Processing Task")

async def myTaskGenerator():
    for i in range(5):
        asyncio.ensure_future(myTask())

loop = asyncio.get_event_loop()
loop.run_until_complete(myTaskGenerator())
#loop.run_until_complete(asyncio.ensure_future(myTask()))
print("Completed All Tasks")
loop.close()