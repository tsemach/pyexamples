"""
<description>
from: https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

Pros
    It's a true class

Cons
    Multiple inheritance - eugh! __new__ could be overwritten
    during inheritance from a second base class? One has to
    think more than is necessary.
</description>

<output>
</output>
"""


class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class MyClass(Singleton):
    pass
