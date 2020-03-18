"""
from: https://www.youtube.com/watch?v=HUtLnn5MBGk&t=30s
"""

from weakref import WeakKeyDictionary


class AgeDescriptor(object):
    def __init__(self):
        self._age = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self._age[instance]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("age must be int")
        if value < 0 or value > 120:
            raise ValueError("age must be int 0:120")
        self._age[instance] = value

    def __delete__(self, instance):
        del self._age[instance]


class Person(object):
    _age = AgeDescriptor()

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return "{0} is {1} " \
               "years old".format(self._name, self._age)


o1 = Person("Me", 20)
print(o1)
o2 = Person("You", 30)
print(o2)
print(o1)

