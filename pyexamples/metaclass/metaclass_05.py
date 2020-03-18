"""
<description>
from: http://masnun.com/2016/05/03/python-metaclass-explained.html

Keep count of number of subclass of me.

Note: TrackSubclasses is called on EVERY class definition.                                        
So the deceleration class A(metaclass=TrackSubclasses) ...
is creation of class A object that's way TrackSubclasses is called
</description>

<output>
TrackSubclasses:__init__ called
TrackSubclasses:__init__ called
TrackSubclasses:__init__ called
TrackSubclasses:__init__ called
{<class '__main__.A'>: 2, <class '__main__.B'>: 1}
</output>
"""


class TrackSubclasses(type):
    subclasses = {}

    def __init__(cls, name, bases, attrs):
        print("TrackSubclasses:__init__ called")
        for base in bases:
            cls.subclasses[base] = cls.subclasses.get(base, 0) + 1

        super().__init__(name, bases, attrs)


class A(metaclass=TrackSubclasses):
    def __init__(self):
        print("A:__init__ called")
    pass


class B(A):
    def __init__(self):
        print("B:__init__ called")
    pass


class C(A):
    def __init__(self):
        print("C:__init__ called")
    pass


class D(B):
    def __init__(self):
        print("D:__init__ called")
    pass


print(TrackSubclasses.subclasses)
