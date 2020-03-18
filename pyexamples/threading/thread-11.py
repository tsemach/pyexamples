import logging
import threading
import time

"""
<description>
from: https://pymotw.com/3/threading/

Event objects are a simple way to communicate between threads safely. An Event manages an internal 
flag that callers can control with the set() and clear() methods. Other threads can use wait() to 
pause until the flag is set, effectively blocking progress until allowed to continue.

The wait() method takes an argument representing the number of seconds to wait for the event before 
timing out. It returns a Boolean indicating whether or not the event is set, so the caller knows 
why wait() returned. The is_set() method can be used separately on the event without fear of blocking.
</description>

<output>
(block     ) wait_for_event starting
(nonblock  ) wait_for_event_timeout starting
(MainThread) Waiting before calling Event.set()
(nonblock  ) event set: False
(nonblock  ) doing other work
(nonblock  ) wait_for_event_timeout starting
(nonblock  ) event set: False
(nonblock  ) doing other work
(nonblock  ) wait_for_event_timeout starting
(nonblock  ) event set: False
(nonblock  ) doing other work
(nonblock  ) wait_for_event_timeout starting
(nonblock  ) event set: False
(nonblock  ) doing other work
(nonblock  ) wait_for_event_timeout starting
(MainThread) Event is set
(nonblock  ) event set: True
(nonblock  ) processing event
(block     ) event set: True
</output>
"""

def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    """wait_for_event() blocks on the call to wait(), which does not return until the event status changes."""

    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)


def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    """wait_for_event_timeout() checks the event status without blocking indefinitel"""

    while not e.is_set():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

e = threading.Event()
t1 = threading.Thread(
    name='block',
    target=wait_for_event,
    args=(e,),
)
t1.start()

t2 = threading.Thread(
    name='nonblock',
    target=wait_for_event_timeout,
    args=(e, 0.2),
)
t2.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(0.9)
e.set()
logging.debug('Event is set')
