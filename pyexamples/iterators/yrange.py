
"""
from: http://anandology.com/python-practice-book/iterators.html

Whats make object iterator - iterator protocol
1) implement the method __iter__ which return an iterator object
2) implement __next__() which move to next item - change in python3 to from next to __naxt__
3) rais StopIteration when iterator reach to its end

"""


class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

if __name__ == "__main__":
    y = yrange(5)
    print("print with __next()__ method")
    while True:
        try:
            print(y.__next__())
        except StopIteration as e:
            print(e)
            break;

    print("print with list")
    print(list(yrange(5)))

    print("\nprint with implicit iter()/next() method")
    for x in yrange(5):
        print(x)

    print("\nprint with explicit iter()/next() method")
    i = iter(yrange(5))
    while True:
        try:
            print(next(i))
        except StopIteration as e:
            print(e)
            break

