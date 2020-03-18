import abc

"""
SanityBase:
    use as base class for all sanity checks.
"""


class SanityBase(object):
    _sanity = {}
    _mapping = {}

    def prepare(self, *argc, **kwargs):
        """prepare for sanity, like load config et c.. ."""
        return

    def run(self):
        """run sanity check on"""
        print("SanityBase: run is called")

    def name(self):
        """return the name of a validator"""
        print("SanityBase: name is called")

    @classmethod
    def init(cls):
        cls._sanity = {}
        cls._mapping = {}

    def create(cls, what, args=[]):
        print("SanityBase: what if {}, args is {}".format(what, args))

    @classmethod
    def mapping(cls, name, clazz):
        print("SanityBase: mapping name '{} to '{}'".format(name, clazz))


if __name__ == "__main__":
    sanity = SanityBase()
    sanity.init()
    sanity.name()
    sanity.create("size", None)
    sanity.mapping("size", None)
    sanity.run()
