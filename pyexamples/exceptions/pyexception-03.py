"""
from: https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/

A useful pattern when dealing with exceptions is the bare raise. 
Normally, raise is paired with an exception to be raised. 
However, if it's used *in exception handling code*, raise has a slightly different (but immensely useful) meaning.

if we have no intention of actually handling the exception. Ideally, we want to an exception raised in _do_calculation to be flow back to the user code as normal. 
If we simply raised a new exception from our except clause, the traceback point to our except clause and mask the real issue (not to mention confusing the user). 
raise on its own, however, lets the exception propagate normally with its original traceback. 
In this way, we record the information we want and the user is able to see what actually caused the exception
"""


def calculate_value(self, foo, bar, baz):
    try:
        result = self._do_calculation(foo, bar, baz)
    except:
        self.user_screwups += 1 
        raise
    return result
