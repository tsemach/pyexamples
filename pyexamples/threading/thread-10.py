import threading
import time
import logging

"""
<description>
from: https://pymotw.com/3/threading/                                           

By default, join() blocks indefinitely.                                 
</description>

<output>
(daemon    ) Starting
(non-daemon) Starting
main: waiting for threads to complete
(non-daemon) Exiting
main: all threads to completed except daemon thread
</output>
"""

def daemon():
    logging.debug('Starting')
    time.sleep(10)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=daemon, daemon=True)
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

print("main: waiting for threads to complete")
t.join()
time.sleep(2)

print("main: all threads to completed except daemon thread")
