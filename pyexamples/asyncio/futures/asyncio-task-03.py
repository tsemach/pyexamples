import asyncio

"""
<description>
from: http://masnun.com/2015/11/20/python-asyncio-future-task-and-the-event-loop.html

Python asyncio: Future, Task and the Event Loop | Abu ...
Event Loop On any platform, when we want to do something asynchronously, it usually involves an event loop. 
An event loop is a loop that can register tasks to be ...

A Future is an object that is supposed to have a result in the future.
A Task is a subclass of Future that wraps a coroutine.
When the coroutine finishes, the result of the Task is realized.

flow:
  - @asyncio.coroutine declares it as a coroutine
  - loop.create_task(slow_operation()) creates a task from the coroutine returned by slow_operation()
  - task.add_done_callback(got_result) adds a callback to our task
  - loop.run_forever(task) runs the event loop until specific stop
</description>

<output>
Future is done!
</output>
"""

async def slow_operation():
    await asyncio.sleep(1)
    return 'Future is done!'


def got_result(future):
    print(future.result())

    # We have result, so let's stop
    loop.stop()


loop = asyncio.get_event_loop()
task = loop.create_task(slow_operation())
task.add_done_callback(got_result)

# We run forever
loop.run_forever()
