import abc

"""
SanityBase:
    use as base class for all sanity checks.
    - prepare(): is an abstract method which should called before the sanity checks.
    - run(): an abstract method which the drive class implement for doing his checks.
    - init(): class method to collect all subclasses inherit from SanityBase and store them in sanity dict
              for factory purpose.
    - create(): a class method use as factory. the what is a the class name need to instantiate.  
"""


class SanityBase(object):
    __metaclass__ = abc.ABCMeta
    _sanity = {}
    _mapping = {}

    @abc.abstractmethod
    def prepare(self, *argc, **kwargs):
        """prepare for sanity, like load config et c.. ."""
        return

    @abc.abstractmethod
    def run(self):
        """run sanity check on"""
        print('SanityBase: run is called')

    @abc.abstractmethod
    def name(self):
        """return the name of a validator"""
        print('SanityBase: name is called')

    @classmethod
    def init(cls):
        cls._sanity = {}
        cls._mapping = {}
        types = cls.__subclasses__()
        for c in types:
            cls._sanity[c.__name__] = c
            cls._mapping[c.name()] = c.__name__

    @classmethod
    def create(cls, what, args=[]):
        print("SanityBase: init is called")

    @classmethod
    def mapping(cls, name, clazz):
        print("SanityBase: init is called")

    @classmethod
    def print(cls):
        print("SanityBase:print is called")
        for n in cls._mapping:
            print("SanityBase:print name '{}' to linked to '{}'".format(n, cls._sanity[cls._mapping[n]]))


if __name__ == "__main__":
    """implement drive class just for test"""
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

    """check init is working"""
    SanityBase.init()
    SanityBase.print()
