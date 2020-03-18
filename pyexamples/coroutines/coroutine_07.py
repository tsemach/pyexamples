"""
from: http://www.geeksforgeeks.org/coroutine-in-python/
Python3 program for demonstrating
coroutine chaining
"""


def producer(sentence, next_coroutine):
    """
    Producer which just split strings and
    feed it to pattern_filter coroutine
    """
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
    """
    Search for pattern in received token
    and if pattern got matched, send it to
    print_token() coroutine for printing
    """
    print("pattern_filter: searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("pattern_filter: done with filtering!!")


def print_token():
    """
    Act as a sink, simply print the
    received tokens
    """
    print("print_token: I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(f"print_token: {token}")
    except GeneratorExit:
        print("print_token: done with printing!")


pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine=pt)
pf.__next__()

sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)
