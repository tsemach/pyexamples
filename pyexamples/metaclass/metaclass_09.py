
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
I am MyClass3 - 0 - 0x7f8d8e7e3be0
I am MyClass3 - 1 - 0x7f8d8e7e3c18
I am MyClass3 - 2 - 0x7f8d8e7e3c50
I am MyClass3 - 3 - 0x7f8d8e7e3be0
I am MyClass3 - 4 - 0x7f8d8e7e3c18
I am MyClass3 - 5 - 0x7f8d8e7e3c50
I am MyClass3 - 6 - 0x7f8d8e7e3be0
I am MyClass3 - 7 - 0x7f8d8e7e3c18
</output>
"""


class Pool(type):
    _instances = {}
    _max_objects = 3

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = (0, [super(Pool, cls).__call__(*args, **kwargs)])

            return cls._instances[cls][1][0]

        i = cls._instances[cls][0] + 1
        a = cls._instances[cls][1]
        if i < cls._max_objects:
            if i < len(a):
                cls._instances[cls] = (i, a)

                return a[i]

            a.append(super(Pool, cls).__call__(*args, **kwargs))
            cls._instances[cls] = (i, a)

            return a[-1]

        # rotate the pool from the beginning
        cls._instances[cls] = (0, cls._instances[cls][1])

        return cls._instances[cls][1][0]


# Python3
class MyClass3(metaclass=Pool):
    def __init__(self, i):
        self._i = i

    def print(self):
        print("I am MyClass3 - {} - {}".format(i, hex(id(self))))


print("main: start now")
for i in range(8):
    a = MyClass3(i)
    a.print()
