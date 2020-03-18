"""
<description>
Show an example of using __getitem__ magic method.                                                                                                        
</description>
<output>
1
2
3
<class '__main__.SimpleList'>
<class 'iterator'>
1
2
3
Expecting StopIteration
Traceback (most recent call last):
  File "getitem-03.py", line 21, in <module>
    print(next(it))
StopIteration
</output>
"""
class SimpleList(object):
    def __init__(self, *items):
        self.items = items

    def __getitem__(self, i):
        return self.items[i]


it = iter(SimpleList(1, 2, 3))
for i in it:
    print(i)

print(type(SimpleList(1, 2, 3)))
print(type(iter(SimpleList(1, 2, 3))))

it = iter(SimpleList(1, 2, 3))
print(next(it))
print(next(it))
print(next(it))
print("Expecting StopIteration")
print(next(it))
