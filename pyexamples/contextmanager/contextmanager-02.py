"""
from: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

Example of creating our own context manager:
the File object implement the context-manager protocol

"""


class File(object):
    def __init__(self, filename, mode):
        print("File::__init__() is called")
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("File::__enter__() is called")
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        print("File::__exist__() is called")
        self.open_file.close()

files = []
for _ in range(10):
    with File('some.output', 'w') as infile:
        infile.write('foo')
        files.append(infile)
print("\nmain(): size of files is - {}".format(len(files)))
