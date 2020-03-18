import os
from step_05 import SanityBase


class SanitySize(SanityBase):
    def __init__(self, args=[]):
        self._args = args
        self._size = 1024

    @staticmethod
    def name():
        return 'size'

    def prepare(self, *args, **kwargs):
        self._size = args[0]

    def run(self):
        for f in os.listdir("."):
            if os.path.getsize(f) > self._size:
                print("SanitySize:run size of {} larger then {}".format(f, self._size))


if __name__ == "__main__":
    SanityBase.init()
    s = SanityBase.create("size")
    s.prepare(1024)
    s.run()
