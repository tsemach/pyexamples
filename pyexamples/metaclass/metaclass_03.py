"""
<description>
from: http://masnun.com/2016/05/03/python-metaclass-explained.html

create a class object which is final.
there is no way to inherit from a class built by Final metaclass                                
</description>

<output>
Traceback (most recent call last):
  File "metaclass_03.py", line 26, in <module>
    class ChildClass(FinalClass):
  File "metaclass_03.py", line 15, in __init__
    raise TypeError("{} is final".format(klass.__name__))
TypeError: FinalClass is final
</output>
"""


class Final(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

        for klass in bases:
            if isinstance(klass, Final):
                raise TypeError("{} is final".format(klass.__name__))


class FinalClass(metaclass=Final):
    def __init__(self):
        print("FinalClass:__init__ called")

    def print(self):
        print("FinalClass:print: I am FinalClass")


class ChildClass(FinalClass):
    def __init__(self):
        print("ChileClass:__init__ is called")

    def print(self):
        print("FinalClass:print: I am ChileClass")


a = FinalClass()
a.print()
b = ChildClass()
b.print()
