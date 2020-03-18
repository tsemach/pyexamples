from singleton import singleton


@singleton
class Foo:
    def __init__(self, name):
        self._name = name
        print('Foo created, name = {}'.format(name))

    def bar(self, obj):
        print(obj)

    def __str__(self):
        return self._name


if __name__ == "__main__":
    foo = Foo("C0")    # Good; prints 'Foo created'
    goo = Foo("C1")    # Already created, prints nothing
    print(hex(id(Foo("C0"))))
    print(hex(id(Foo("C1"))))
    print(hex(id(Foo("C2"))))
    print(foo)
    print(goo)
    print(goo is foo)       # True

    foo.bar('Hello, world! I\'m a singleton.')
    for i in range(5):
        print(f'for with else {i}')
    else:
        print('else of for is called {}'.format(i))
