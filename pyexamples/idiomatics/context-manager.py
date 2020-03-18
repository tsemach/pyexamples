import os
import sys
import contextlib


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


# Do: use ignored to ignore exception
divider()
print("Do: use ignored to ignore exception\n")

with contextlib.suppress(OSError):
    print('before call to remove file.not.exist')
    os.remove('file.not.exist')
    print('no exception called')

divider(is_end=True)

# Do: write you own ignore
divider()
print('Do: write you own ignore\n')


@contextlib.contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass


with ignored(OSError):
    print('before call to remove file.not.exist')
    os.remove('file.not.exist')
    print('no exception called')

divider(is_end=True)
