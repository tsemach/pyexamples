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
        print("SanityBase: init is called")

    @classmethod
    def create(cls, what, args=[]):
        print("SanityBase: init is called")

    @classmethod
    def mapping(cls, name, clazz):
        print("SanityBase: init is called")


if __name__ == "__main__":
    sanity = SanityBase()
    sanity.init()
    sanity.init()
    sanity.name()
    sanity.create("size", None)
    sanity.mapping("size", None)
