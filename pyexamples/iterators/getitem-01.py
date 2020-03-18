"""
<description>
Iterator example without __iter__ and __next__

__getitem__ is define so
    - a isinstance of SimpleList
    - then a[i] is roughly equivalent to type(x).__getitem__(x, i)

there are two ways of iterate SimpleList one by iter(SimpleList(1, 2, 3)) other
by using a = SimpleList(1, 2, 3), a[0], a[1], a[2].1
</description>

<output>
print items with next(it)
1
2
3


print items with a[]
1
2
3
</output>
"""


class SimpleList(object):
    def __init__(self, *items):
        self._items = items

    def __getitem__(self, i):
        return self._items[i]

a = SimpleList(1, 2, 3)
it = iter(a)
print('it is {}'.format(it))
print('\n')
print('print items with next(it)')
print(next(it))
print(next(it))
print(next(it))

a = SimpleList(1, 2, 3)
print('\n')
print('print items with a[]')
print(a[0])
print(a[1])
print(a[2])
