"""
from: https://www.ibm.com/developerworks/library/os-pythondescriptors/index.html

You can create a descriptor a number of ways:
_____________________________________________
Create a class and override any of the descriptor methods: __set__, __ get__, and __delete__.
This method is used when the same descriptor is needed across many different classes and attributes,
for example, for type validation.
Use a property type which is a simpler and more flexible way to create a descriptor.
Use the power of property decorators which are a combination of property type method and Python decorators.
"""


class Descriptor(object):

    def __init__(self):
        self._name = ''

    def __get__(self, instance, owner):
        print('Descriptor:__get__: getting: %s' % self._name)
        return self._name

    def __set__(self, instance, name):
        print("Descriptor:__set__: setting: %s" % name)
        self._name = name.title()

    def __delete__(self, instance):
        print("Descriptor:__deleting: %s" % self._name)
        del self._name


class Person(object):
    name = Descriptor()


p = Person()
p.name = 'tsemach mizrachi'
print(p.name)
