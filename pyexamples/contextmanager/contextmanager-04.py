
"""
from: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

The decorator generate another function behind the scenes which wrap the defined method

Using the @contextmanager decorator.
- The decorate a generator function that calls yield exactly once.
- Everything before the call to yield is considered the code for __enter__().
- Everything after is the code for __exit__().

So: in open_file
    the_file = open(path, mode) - is called on __enter__ and the_file is yield
    the_file.close() is called on __exist__
"""

from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    print("open-file() is called")
    the_file = open(path, mode)
    yield the_file
    print("open-file() after yield")
    the_file.close()

files = []

for x in range(10):
    with open_file('foo.txt', 'w') as infile:
        files.append(infile)

for f in files:
    if not f.closed:
        print('not closed')