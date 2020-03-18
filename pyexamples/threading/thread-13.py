import threading
import logging

"""
<description>
from: https://pymotw.com/3/threading/

Locks implement the context manager API and are compatible with the with statement. 
Using with removes the need to explicitly acquire and release the lock.

The two functions worker_with() and worker_no_with() manage the lock in equivalent ways.
</description>

<output>
(Thread-1  ) Lock acquired via with
(Thread-2  ) Lock acquired directly
</output>
"""

def worker_with(lock):
    with lock:
        logging.debug('Lock acquired via with')


def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()
