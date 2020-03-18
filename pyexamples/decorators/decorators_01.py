
"""
from: http://masnun.com/2016/04/03/understanding-decorators-in-python.html

Decorators are callable (functions classes),  that wrap other callable.

By definition, a Decorator is a callables which takes a callable and returns a callable.
A callable can be a few things like functions, classes etc.
In most cases, a decorator just takes a function, wraps it and returns the wrapped function.
The wrapped function can access a reference to our original function and call it as necessary.
In our case time_wrapper is the decorator function which takes the greet function and returns the new_function.

Output:
    5 time of the following:
    Current time: <current time>
    Hello world!
"""

from time import sleep
from datetime import datetime


def timed(fn):
    def wrapped():
        print("Current time: {}".format(datetime.now()))
        return fn()

    return wrapped


@timed
def hello():
    print("Hello world!")


for x in range(5):
    hello()
    sleep(10)