"""
<description>
__call__:
In Python, functions are first-class objects, this means: function references can be passed in
inputs to other functions and/or methods, and executed from inside them.
Instances of Classes (aka Objects), can be treated as if they were functions: pass them to other
methods/functions and call them. In order to achieve this, the __call__ class function has to be specialized.

def __call__(self, [args ...]) It takes in input a variable number of arguments. Assuming x being an
instance of the Class X, x.__call__(1, 2) is analogous to calling x(1,2) or the instance itself
as a function.

In Python, __init__() is properly defined as Class Constructor (as well as __del__() is the Class Distructor).
Therefore, there is a net distinction between __init__() and __call__(): the first builds an
instance of Class up, the second makes such instance callable as a function would be without
impacting the lifecycle of the object itself (i.e. __call__ does not impact the construction/destruction
lifecycle) but it can modify its internal state (as shown below).
</description>

<output>

Show example-1
----------------
__call__ with (7,8)

Show example-2
----------------
A: init is called
A: init is called
A: __call__ is called
</output>
"""

print("\nShow example-1")
print("----------------")


class Stuff(object):
    """Example-1: """
    def __init__(self, x, y, range):
        super(Stuff, self).__init__()
        self.x = x
        self.y = y
        self.range = range

    def __call__(self, x, y):
        self.x = x
        self.y = y
        print('__call__ with (%d,%d)' % (self.x, self.y))

    def __del__(self):
        del self.x
        del self.y
        del self.range

s = Stuff(1, 2, 3)
s(7, 8)

print("\nShow example-2")
print("----------------")


class A:
    def __init__(self):
        print("A: init is called")

    def __call__(self):
        print("A: __call__ is called")

A()
A()()
