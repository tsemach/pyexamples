"""
from: https://www.ibm.com/developerworks/library/os-pythondescriptors/index.html

All the preceding examples operate with the name attribute.
The limitation of this approach is the necessity of separately
overriding __set__(), __get__() and __delete__() for each attribute.
Listing 5 provides a possible solution when a developer wishes to
add property attributes at run time. This uses property type to build
a data descriptor.
"""


class Person(object):

    def add_property(self, attribute):
        # create local setter and getter with a particular attribute name
        getter = lambda self: self._get_property(attribute)
        setter = lambda self, value: self._set_property(attribute, value)

        # construct property attribute and add it to the class
        setattr(self.__class__, attribute, property(fget=getter, \
                                                    fset=setter, \
                                                    doc="Auto-generated method"))

    def _set_property(self, attribute, value):
        print("Person:_set_property: setting: %s = '%s'" % (attribute, value))
        setattr(self, '_' + attribute, value.title())

    def _get_property(self, attribute):
        print("Person:_get_property: getting: attribute is '%s'" % attribute)
        return getattr(self, '_' + attribute)


p = Person()
p.add_property('name')
p.name = 'tsemach mizrachi'
print(p.name)
p.name = "more name"
print(p.name)
