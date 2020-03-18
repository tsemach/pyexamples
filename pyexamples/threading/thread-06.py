import threading
import time
import logging

"""
<description>
from: https://pymotw.com/3/threading/
By default, join() blocks indefinitely. It is also possible to pass a float value representing 
the number of seconds to wait for the thread to become inactive. If the thread does not 
complete within the timeout period, join() returns anyway.

To wait until a daemon thread has completed its work, use the join() method.
</description>

<output>
(daemon    ) Starting
main: waiting for threads to complete
(non-daemon) Starting
d.isAlive() True
(non-daemon) Exiting
main: all threads to completed except daemon thread
</output>
"""

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    time.sleep(1)
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
d.join(0.1)
print('d.isAlive()', d.isAlive())
t.join()

print("main: all threads to completed except daemon thread")
