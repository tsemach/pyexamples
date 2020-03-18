"""
<description>
from: https://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute#3278104

Difference between __getattr__ vs __getattribute__
1) __getattr__: called if attribute is not exist
2) __getattribute__ : is invoked before looking at any actual attributes on the object

__getattribute__ can use to protect access to some attributes.

Notes:
A) Infinity loop:
    In order to avoid infinite recursion in __getattribute__
    method, its implementation should always call the base class
    method with the same name to access any attributes it needs.
    For example: object.__getattribute__(self, name) or super().__getattribute__(item)
    and not self.__dict__[item]
B) if a class include both __getattr__ and __getatribute__
   then __getattribute__ called first. Unless exception  is raise
   If  __getattribute__ raises  AttributeError exception
   then the exception will be ignored and __getattr__ method will be invoked
</description>

<output>
1
10
Count:__getattr__ is called
0
</output>
"""


class Count:
    def __init__(self, the_min, the_max):
        self._min = the_min
        self._max = the_max

    def __getattr__(self, item):
        print("Count:__getattr__ is called")
        self.__dict__[item] = 0

        return 0


o = Count(1, 10)
print(o._min)
print(o._max)
print(o.anyother)

