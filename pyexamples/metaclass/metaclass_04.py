"""
<description>
from: https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

Pros
    It's a true class
    Auto-magically covers inheritance
    Uses __metaclass__ for its proper purpose (and made me aware of it)

Cons
    Are there any?
</description>

<output>
main: start now
Singleton:__call__ is called
I am MyClass3 - 0x7ff4da4a5b00
Singleton:__call__ is called
I am MyClass3 - 0x7ff4da4a5b00
Singleton:__call__ is called
I am MyClass3 - 0x7ff4da4a5b00
</output>
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("Singleton:__call__ is called")
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Python3
class MyClass3(metaclass=Singleton):
    pass

    def print(self):
        print("I am MyClass3 - {}".format(hex(id(self))))


print("main: start now")
a = MyClass3()
a.print()
b = MyClass3()
b.print()
c = MyClass3()
c.print()
