
from step_01 import SanityBase


class SanitySize(SanityBase):
    def __init__(self, args=[]):
        self._args = args

    @staticmethod
    def name():
        return 'size'

    def prepare(self, *args, **kwargs):
        print("SanitySize: prepare is called")

    def run(self):
        print("SanitySize: run is called")


if __name__ == "__main__":
    size = SanitySize()
    size.init()
    size.prepare()
    print("SanitySize: size.name is '{}'".format(size.name()))
    size.run()
