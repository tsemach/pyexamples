from singleton import singleton


@Singleton
class Foo:
    def __init__(self, name):
        self._name = name
        print('Foo created, name = {}'.format(name))

    def bar(self, obj):
        print(obj)

    def __str__(self):
        return self._name

# foo = Foo()  # Wrong, raises SingletonError


foo = Foo("C0")    # Good; prints 'Foo created'
goo = Foo("C1")    # Already created, prints nothing
print(hex(id(foo)))
print(hex(id(goo)))
print(foo)
print(goo)
print(goo is foo)       # True

foo.bar('Hello, world! I\'m a singleton.')

