"""
<description>
                                                                            
</description>

<output>
data:__init__ enter to ..
data:prop:__init__ n is 4
<class '__main__.data.prop'>
data:__init_ n = 4, hex(id) is 0x7f44178afb70
data:prop:__getattribute__ item _n
<class '__main__.data.prop'>
</output>
"""


class data(object):
    class prop(object):
        def __init__(self, n):
            print(f"data:prop:__init__ n is {n}")
            self._n = n

        def __eq__(self, other):
            print(f"data:prop:__eq__ other is {other}")
            return self._n == other

        def __getattribute__(self, item):
            print(f'data:prop:__getattribute__ item {item}')

    def __init__(self, n):
        print('data:__init__ enter to ..')
        self.prop = data.prop(n)
        print(type(self.prop))
        print(f"data:__init_ n = {n}, hex(id) is {hex(id(self.prop))}")

    def fn(self, other):
        print(f'fn is oterh {other}')

    def __eq__(self, other):
        print(f'data:__eq__: other is {other}')
        return self.prop == other

d = data(4)
i = d.prop._n
print(type(d.prop))
