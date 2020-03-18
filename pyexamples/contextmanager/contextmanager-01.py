"""
from: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

A context manager object is an object which implement __enter__ and __exist__ method.
So on initiate the __enter__ is called to consume some resource and doing initialization work
while __exist__ is called when the variable (infile in this case) is out of scope
open(..) return a context-manager object.

"""
with open('some.data', 'r') as infile:
    for line in infile:
        print('> {}'.format(line.strip()))