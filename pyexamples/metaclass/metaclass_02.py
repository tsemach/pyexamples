"""
<description>
from: from: http://masnun.com/2016/05/03/python-metaclass-explained.html

Simple class object creation.
</description>

<output>
True
<class '__main__.MetaClass'>
</output>
"""


class MetaClass(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.is_meta = True


class MyClass(metaclass=MetaClass):
    pass


print(MyClass.is_meta)
print(type(MyClass))
