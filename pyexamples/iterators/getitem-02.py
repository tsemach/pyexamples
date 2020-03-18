"""
<description>
Iterator example without __iter__ and __next__

__getitem__ is define so
    - a isinstance of GetItemTest
    - then a[i] is roughly equivalent to type(x).__getitem__(x, i)

there are two ways of iterate GetItemTest one by iter(GetItemTest(1, 2, 3)) other
by using a = GetItemTest(1, 2, 3), a[0], a[1], a[2].1
</description>
<output>
</<class 'int'>    1
<class 'str'>    hello world
<class 'tuple'>  (1, 'b', 3.0)
<class 'slice'>  slice(5, 200, 10)
<class 'slice'>  slice('a', 'z', 3)
<class 'object'> <object object at 0x7f9ca7d0a090>
</output>
"""


class GetItemTest(object):
    def __getitem__(self, items):
        print('%-16s %s' % (type(items), items))

t = GetItemTest()
t[1]
t['hello world']
t[1, 'b', 3.0]
t[5:200:10]
t['a':'z':3]
t[object()]
