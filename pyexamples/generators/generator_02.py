import os

"""
scan directories and print their path including subdirectories

The dirlist is a generator. calling to it just return a generator object.
the for loop in line 21 is the calling next() on the generator (which is a type of iterator)
start execute the method until yield is call on line 14. Value of file is returned but the 
method is stay on its state waiting for next call to next() method until end of files list
then StopIteration is raise (according to iterator protocol). 
"""


def dirlist(dirname):
    files = os.listdir(dirname)
    for file in files:
        yield file


def scan(name):
    if os.path.isfile(name):
        print(name)
        return
    if os.path.isdir(name):
        for f in dirlist(name):
            scan(name + "/" + f)


if __name__ == "__main__":
    scan(".")
