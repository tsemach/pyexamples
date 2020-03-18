"""
from: https://www.ibm.com/developerworks/library/os-pythondescriptors/index.html

While the descriptor specified in 'descriptor_01.py' is valid and functional,
another method is through the property type.
With the property(), it is easy to create a usable descriptor for any
attribute.
The syntax for creating property() is property(fget=None, fset=None, fdel=None, doc=None) where:
"""


class Person(object):

    def __init__(self):
        print("Descriptor:__init__: enter to ..")
        self._name = ''

    def fget(self):
        print("Descriptor:fget: getting: %s" % self._name)
        return self._name

    def fset(self, value):
        print("Descriptor:fset: %s" % value)
        self._name = value.title()

    def fdel(self):
        print("Descriptor:fdel: deleting: %s" % self._name)
        del self._name

    name = property(fget, fset, fdel, "I'm the property.")


p = Person()
print(type(p.name))
p.name = 'tsemach mizrachi'
print(type(p.name))
print(p.name)
