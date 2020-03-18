class SingletonError(Exception):
    pass


class singleton:

    _singletons = dict()

    def __init__(self, decorated):
        self._decorated = decorated

    def __call__(self, *args, **kwargs):
        print("singleton:__call__ is called")
        key = self._decorated.__name__

        try:
            return singleton._singletons[key]
        except KeyError:
            singleton._singletons[key] = self._decorated(*args, **kwargs)

            return singleton._singletons[key]


if __name__ == "__main__":
    @singleton
    class Foo:
        def __init__(self, name):
            self._name = name
            print('Foo created, name = {}'.format(name))

        def bar(self, obj):
            print(obj)

        def __str__(self):
            return self._name

    foo = Foo("C0")    # Good; prints 'Foo created'
    goo = Foo("C1")    # Already created, prints nothing
    print(hex(id(Foo("C0"))))
    print(hex(id(Foo("C1"))))
    print(hex(id(Foo("C2"))))
    print(foo)
    print(goo)
    print(goo is foo)       # True

    foo.bar('Hello, world! I\'m a singleton.')