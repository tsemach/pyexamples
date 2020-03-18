import random
import threading
import time
import logging

"""
<description/
from: https://pymotw.com/3/threading/

It is not necessary to retain an explicit handle to all of the daemon threads in order to ensure 
they have completed before exiting the main process. enumerate() returns a list of active Thread 
instances. The list includes the current thread, and since joining the current thread introduces 
a deadlock situation, it must be skipped.
</description>

<output>
(Thread-1  ) sleeping 0.10
(Thread-2  ) sleeping 0.50
(Thread-3  ) sleeping 0.40
(MainThread) joining Thread-1
(Thread-1  ) ending
(MainThread) joining Thread-2
(Thread-3  ) ending
(Thread-2  ) ending
(MainThread) joining Thread-3
</output>
"""


def worker():
    """thread worker function"""
    pause = random.randint(1, 5) / 10
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(3):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()
