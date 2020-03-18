
def memoize(f):
    cache = {}

    def inner(*args, **kwargs):
        if args not in cache:
            cache[args] = f(*args, **kwargs)
        return cache[args]

    inner.__name__ = 'memoized_' + f.__name__

    return inner


@memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))