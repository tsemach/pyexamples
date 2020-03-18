"""
from: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

This example show using a cantext-manager to make sure lock object is always release without deadlock.

"""

from threading import Lock

lock = Lock()


def do_something_dangerous():
    with lock:
        raise Exception('oops I forgot this code could raise exceptions')

try:
    do_something_dangerous()
except:
    print('Got an exception')
lock.acquire()
print('Got here')
