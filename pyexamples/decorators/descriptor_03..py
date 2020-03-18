"""
from: https://www.ibm.com/developerworks/library/os-pythondescriptors/index.html

Defining read only property:
The syntax for creating property() is property(fget=None, fset=None, fdel=None, doc=None)

Note here that fget, fset and fdel methods are optional,
but if one is not specified, an exception of AttributeError is raised
when the respective operation is attempted.

For example, a name property is declared with None as fset, and then
the developer tries to assign value to name attribute.
An exception AttributeError is raised.
"""


class Person(object):

    def __init__(self, name):
        self._name = name.title()

    def fget(self):
        print("Descriptor:fget: getting: %s" % self._name)
        return self._name

    def fset(self, value):
        print("Descriptor:fset: %s" % value)
        self._name = value.title()

    def fdel(self):
        print("Descriptor:fdel: deleting: %s" % self._name)
        del self._name

    name = property(fget, None, fdel, "I'm the property.")


p = Person('tsemach mizrachi')
try:
    p.name = 'tsemach mizrachi'
except AttributeError:
    print("main: ERROR unable to set value to p.name")

print(p.name)
