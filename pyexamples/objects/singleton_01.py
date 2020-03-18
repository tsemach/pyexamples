
"""
This class is an example of specific class (DBDriver) singleton.

"""


class SingletonException(Exception):
    pass


class DBDriver:
    # store the instance
    _instance = None

    def __init__(self):
        if DBDriver._instance is not None:
            raise SingletonException("all ready created, use DBDriver.instance()")
        else:
            DBDriver._instance = self

    @staticmethod
    def instance():
        if DBDriver._instance is None:
            DBDriver()

        return DBDriver._instance


d1 = DBDriver.instance()
print(d1)
d2 = DBDriver.instance()
print(d2)
assert d1 == d2

d3 = DBDriver()
