import time

"""
<description>
This example show the use of __getattribute__ to "shutdown" an object.
After self._is_done is True any call to a method will raise RuntimeError exception 

Note: this technique works only on methods not on class variables 
</description>

<output>
Foo:__getattribute__: show
Foo:__getattribute__: _foo
Foo:print: In main-1
Foo:__getattribute__: _is_done
Foo:__getattribute__: item = _is_done
Foo:__getattribute__: item = type(item) = <class 'str'>
Traceback (most recent call last):
  File "attribute_05.py", line 38, in <module>
    print(f"\ngoing to set f._is_done: {f._is_done}")
  File "attribute_05.py", line 31, in __getattribute__
    raise RuntimeError("object is done!!")
RuntimeError: object is done!!
</output>
"""


class Foo(object):
    def __init__(self):
        self._foo = "I am foo"
        self._is_done = False

    def show(self, name):
        print(f"Foo:print: {self._foo}-{name}")
        self._is_done = True

    def __getattribute__(self, item):
        print(f'Foo:__getattribute__: {str(item)}')
        if object.__getattribute__(self, '_is_done'):
            print(f"Foo:__getattribute__: item = {item}")
            print(f"Foo:__getattribute__: item = type(item) = {type(item)}")
            time.sleep(1)
            raise RuntimeError("object is done!!")
        return super().__getattribute__(item)


f = Foo()
f._foo = "In main"
f.show('1')
print(f"\ngoing to set f._is_done: {f._is_done}")
f.show('2')
