import os


def readlines(filename):
    with open(filename) as fp:
        for line in fp:
            yield line


def run():
    lines = readlines("some.data")
    for l in lines:
        print(l.strip())

if __name__ == "__main__":
    run()
