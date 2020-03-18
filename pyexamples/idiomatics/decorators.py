import sys
import random
from functools import wraps

"""
from: https://www.youtube.com/watch?v=OSGv2VnC0go

description: for loop
"""

DIVIDER_LEN = 60


def divider(l=DIVIDER_LEN, is_end=False):
    sys.stdout.write("{}".format('-') * DIVIDER_LEN)
    print('')
    if is_end:
        print('')


# Do: use decorator for caching
divider()
print("Do: use decorator for caching\n")


def cache(func):
    cache = {}

    @wraps(func)
    def inner(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
            print('cache: not found - args:', args, 'value:', cache[args])
            return cache[args]

        print('cache: found - args:', args, 'value:', cache[args])
        return cache[args]

    #inner.__name__ = 'cache' + func.__name__

    return inner

@cache
def cache_me(_):
    return random.randint(1, 5)


for i in range(10):
    cache_me(i)

for i in range(10):
    print('value of', i, 'is:', cache_me(i))

divider(is_end=True)

