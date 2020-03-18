import logging
import random
import threading
import time

"""
<description>
from: https://pymotw.com/3/threading/

Python’s built-in data structures (lists, dictionaries, etc.) are thread-safe as a side-effect of
having atomic byte-codes for manipulating them (the global interpreter lock used to protect Python’s 
internal data structures is not released in the middle of an update). 
Other data structures implemented in Python, or simpler types like integers and floats, do not have 
that protection. To guard against simultaneous access to an object, use a Lock object.

In this example, the worker() function increments a Counter instance, which manages a Lock to prevent 
two threads from changing its internal state at the same time. If the Lock was not used, there is 
a possibility of missing a change to the value attribute.
<description>

<output>
(Thread-1  ) Sleeping 0.13
(Thread-2  ) Sleeping 0.65
(MainThread) Waiting for worker threads
(Thread-1  ) Waiting for lock
(Thread-1  ) Acquired lock
(Thread-1  ) Sleeping 0.57
(Thread-2  ) Waiting for lock
(Thread-2  ) Acquired lock
(Thread-2  ) Sleeping 0.59
(Thread-1  ) Waiting for lock
(Thread-1  ) Acquired lock
(Thread-1  ) Done
(Thread-2  ) Waiting for lock
(Thread-2  ) Acquired lock
(Thread-2  ) Done
(MainThread) Counter: 4
</output>
"""


class Counter:

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)
