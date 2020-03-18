class Singleton:
    """
    Helper class meant to ease the creation of singletons. This
    should be used as a decorator -- not a metaclass -- to the class
    that should be a singleton.

    The decorated class should define only one `__init__` function
    that takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `SingletonError` being raised.
    """

    _singletons = dict()

    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self, *args, **kwargs):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        key = self._decorated.__name__

        try:
            return Singleton._singletons[key]
        except KeyError:
            Singleton._singletons[key] = self._decorated(*args, **kwargs)

            return Singleton._singletons[key]

    def __call__(self):
        """
        Call method that raises an exception in order to prevent creation
        of multiple instances of the singleton. The `Instance` method should
        be used instead.

        """
        raise SingletonError(
            'Singletons must be accessed through the `Instance` method.')


class SingletonError(Exception):
    pass


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


foo = Foo.instance("C0")    # Good; prints 'Foo created'
goo = Foo.instance("C1")    # Already created, prints nothing
print(foo)
print(goo)
print(goo is foo)       # True

foo.bar('Hello, world! I\'m a singleton.')