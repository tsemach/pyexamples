class Count(object):

    def __init__(self, the_min, the_max):
        self._min = the_min
        self._max = the_max
        self.protected = None

    def __getattribute__(self, item):
        if item.startswith('pro'):
            raise AttributeError
        # you can use this one
        # return object.__getattribute__(self, item)
        # or you can use
        return super().__getattribute__(item)


o = Count(1, 10)
print(o._min)
print(o._max)
print(o.protected)
