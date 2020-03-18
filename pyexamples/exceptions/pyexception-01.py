"""
from: https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/

If the object can be coerced to a string, do so and print it. 
If that attempt raises an exception, print our error string. 
Also, note that we're explicitly checking for TypeError, 
which is what would be raised if the coercion failed. 
NEVER use a "bare" except: clause or you'll end up suppressing real errors you didn't intend to catch.

The print() line is only called if no exception was raised. 
If print() raises an exception, this will bubble up the call stack as normal. 
Another use of else is when code in the try block requires some cleanup (and doesn't have a usable context manager),
"""

def print_object(some_object):
    # Check if the object is printable...
    try:
        printable = str(some_object)
        print(printable)
    except TypeError:
        print("unprintable object")


