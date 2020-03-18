import os
from singleton import singleton
from step_05 import SanityBase


@singleton
class SanityFile(SanityBase):
    def __init__(self, args=[]):
        print("SanityFile:__init__ is called")
        self._args = args
        self._prefix = "sanity"

    @staticmethod
    def name():
        return 'file'

    def prepare(self, *args, **kwargs):
        self._prefix = args[0]

    def run(self):
        for f in os.listdir("."):
            if f.startswith(self._prefix):
                print("SanityFile:run file '{}' start with '{}'".format(f, self._prefix))


if __name__ == "__main__":
    SanityBase.init()
    s = SanityBase.create("file")
    print(hex(id(s)))
    s = SanityBase.create("file")
    print(hex(id(s)))
    s.prepare("step")
    s.run()
