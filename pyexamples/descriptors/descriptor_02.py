"""
from: https://docs.python.org/3/howto/descriptor.html

To see how property() is implemented in terms of the descriptor protocol, here is a pure Python equivalent

The important points to remember are:

-) descriptors are invoked by the __getattribute__() method
-) overriding __getattribute__() prevents automatic descriptor calls
-) object.__getattribute__() and type.__getattribute__() make different calls to __get__().
-) data descriptors always override instance dictionaries.
-) non-data descriptors may be overridden by instance dictionaries.
"""


class Property(object):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class User(object):
    def __init__(self, user):
        self.user = user

    def set_user(self, user):
        User.user = user

    def get_user(self):
        return self.user

    user = Property(get_user, set_user)

u = User("tsemach")
print(u.user)

v = User("mizrachi")
print(v.user)
print(u.user)
print(hex(id(v.user)))
print(hex(id(u.user)))
