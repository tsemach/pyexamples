
class data(object):
    class id(object):
        def __eq__(self, other):
            print(f"data:id:__eq__: in id class, other = {other}")
            self.id = other

    def __init__(self, n):
        self._number = n
        self.id = data.id()

    def __setattr__(self, key, value):
        print(f'data:__setattr__: key = {key}, value = {value}')
        super().__setattr__(key, value)

    def __getattribute__(self, item):
        print(f'data:__getattribute__: key = {item}')
        if item == 'id':
            print(f'data:__getattribute__: got id')
            return super().__getattribute__(item)
        return super().__getattribute__(item)

    def the_id(self):
        return 10

    def fn(self, other):
        print(f'fn is oterh {other}')

    def __eq__(self, other):
        print(f'other is {other}')


d = data(4)
print(f'main: {type(d.id)}')
print(f'main: number = {d._number}')
d.id = 5
a = d.id
print(a)
print(type(a))

d.id = 50
a = d.id
print(a)
print(type(a))


