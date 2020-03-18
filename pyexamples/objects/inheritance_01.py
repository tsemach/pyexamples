"""
Inheritance: simple example
<output>
based:print - what is derived
(<class '__main__.Derived'>,)
[<class '__main__.Derived'>]
(<class '__main__.Based'>,)
mro is Derived is (<class '__main__.Derived'>, <class '__main__.Based'>, <class 'object'>)                   
</output>
"""


class Based(object):
    def __init__(self):
        print("Based:__init__ - called")
        self._me = "I am an based"

    def print(self, what):
        print("based:print - what {}".format(what))


class Derived(Based):
    def __init__(self):
        super(Based, self).__init__()


class More(Derived):
    def __init__(self):
        super(Based, self).__init__()


d = Derived()
d.print("is derived")
print(More.__bases__)
print(Based.__subclasses__())
print(Derived.__bases__)
print(f'mro is Derived is {Derived.__mro__}')

