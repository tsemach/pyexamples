"""
from: https://www.ibm.com/developerworks/library/os-pythondescriptors/index.html

Descriptors can be created with Python decorators, as in 'descriptor_03.py
A Python decorator is a specific change to the Python syntax allowing
a more convenient alteration of functions and methods.
In this case, attribute management methods are altered
"""


class Person(object):

    def __init__(self):
        self._name = ''

    @property
    def name(self):
        print("Person:name: getting: %s" % self._name)
        return self._name

    @name.setter
    def name(self, value):
        print("Person:name: setting: %s" % value)
        self._name = value.title()

    @name.deleter
    def name(self):
        print("Person:name: deleting: %s" % self._name)
        del self._name


p = Person()
p.name = 'tsemach mizrachi'
print(p.name)
p.name = "more name"
print(p.name)
