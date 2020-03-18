"""
<description>
http://intermediatepythonista.com/metaclasses-abc-class-decorators

Singleton metaclass is called when the object  instantiate!!                                          
As appose to __new__ and __init__ that is called when create
the class object itself.
</description>

<output>
python3 metaclass_07.py
-----------------------------------
Singleton:__new__ allocating memory for class - Foo
Singleton:__new__ meta is <class '__main__.Singleton'>
Singleton:__new__ bases is (<class 'object'>,)
Singleton:__new__ namespace is {'__module__': '__main__', '__qualname__': 'Foo'}.
Singleton:__init__ is called, cls is Foo
main: start now ..
Singleton:__call__ is called
Singleton:__call__ is called
0x7ff1b0eeecc0
0x7ff1b0eeecc0
True
</output>
"""


class Singleton(type):
    _instances = {}

    def __new__(meta, name, bases, namespace):
        print('-----------------------------------')
        print("Singleton:__new__ allocating memory for class - {}".format(name))
        print("Singleton:__new__ meta is {}".format(meta))
        print("Singleton:__new__ bases is {}".format(bases))
        print("Singleton:__new__ namespace is {}.".format(namespace))
        return super(Singleton, meta).__new__(meta, name, bases, namespace)

    def __init__(cls, name, bases, namespace):
        print("Singleton:__init__ is called, cls is {}".format(cls.__name__))
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print("Singleton:__call__ is called")
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Foo(object, metaclass=Singleton):
    pass


print("main: start now ..")
x = Foo()
y = Foo()
print(hex(id(x)))
print(hex(id(y)))
print(hex(id(y)) == hex(id(x)))
