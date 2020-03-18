
import asyncio

"""
<description>
from: http://masnun.com/2015/11/20/python-asyncio-future-task-and-the-event-loop.html

Python asyncio: Future, Task and the Event Loop | Abu ...
Event Loop On any platform, when we want to do something asynchronously, it usually involves an event loop. An event loop is a loop that can register tasks to be ...
masnun.com
 
A Future is an object that is supposed to have a result in the future.
A Task is a subclass of Future that wraps a coroutine.
When the coroutine finishes, the result of the Task is realized.

flow:
  - @asyncio.coroutine declares it as a coroutine
  - loop.create_task(slow_operation()) creates a task from the coroutine returned by slow_operation()
  - task.add_done_callback(got_result) adds a callback to our task
  - loop.run_until_complete(task) runs the event loop until the task is realized. As soon as it has value, the loop terminates
</description>

<output>
Future is done!
</output>
"""

@asyncio.coroutine
def slow_operation():
    # yield from suspends execution until
    # there's some result from asyncio.sleep

    yield from asyncio.sleep(1)

    # our task is done, here's the result
    return 'Future is done!'


def got_result(future):
    print("get_result() is called ..")
    print(future.result())


# Our main event loop
loop = asyncio.get_event_loop()

# We create a task from a coroutine
task = loop.create_task(slow_operation())

# Please notify us when the task is complete
task.add_done_callback(got_result)

# The loop will close when the task has resolved
loop.run_until_complete(task)
