"""
<description>
from: https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python

Showing three examples of defining abstract classes
</description>

<output>
python2: unable to call to a.foo()
python3.0+: unable to call to a.foo()
Python3.4+: unable to call to a.foo()
</output>
"""

# Python 2
from abc import ABC, ABCMeta, abstractmethod


class Abstract1:
    __metaclass__ = ABCMeta

    @abstractmethod
    def foo(self):
        raise NotImplementedError


# Python 3.0+
class Abstract2(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        print("I am python 3.0+")


# Python 3.4+
class Abstract3(ABC):
    @abstractmethod
    def foo(self):
        print("I am python3.4+")


try:
    a = Abstract1()
    a.foo()
except NotImplementedError:
    print("python2: unable to call to a.foo()")

try:
    a = Abstract2()
    a.foo()
except TypeError:
    print("python3.0+: unable to call to a.foo()")

try:
    a = Abstract3()
    a.foo()
except TypeError:
    print("Python3.4+: unable to call to a.foo()")

