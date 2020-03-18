
import threading
import time
import logging

"""
<description>
from: https://pymotw.com/3/threading/

Sometimes programs spawn a thread as a daemon that runs without blocking the main program 
from exiting. Using daemon threads is useful for services where there may not be an easy way 
to interrupt the thread, or where letting the thread die in the middle of its work does not 
lose or corrupt data (for example, a thread that generates “heart beats” for a service monitoring tool). 
To mark a thread as a daemon, pass daemon=True when constructing it or call its set_daemon() method 
with True. The default is for threads to not be daemons.

The output does not include the "Exiting" message from the daemon thread, since all of the 
non-daemon threads (including the main thread) exit before the daemon thread wakes up from the sleep() call.
</description>

<output>
(daemon    ) Starting
(non-daemon) Starting
(non-daemon) Exiting
(daemon    ) Exiting
main: is end
</output>
"""


def daemon(logging):
    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     format='(%(threadName)-10s) %(message)s',
    # )

    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=daemon, daemon=True, args=(logging,))
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
time.sleep(5)
print("main: is end")
