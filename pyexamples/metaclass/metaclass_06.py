"""
<description>
from: http://intermediatepythonista.com/metaclasses-abc-class-decorators

Imitate class creation
</description>

<output>
{'__init__': <function __init__ at 0x7febe4194158>, 'print': <function print at 0x7febe41941e0>}
tsemach
</output>
"""

class_name = "Foo"
class_parents = (object,)
class_body = """
def __init__(self, name):
    self.name = name

def print(self):
    print(self.name)
"""
# a new dict is used as local namespace
class_dict = {}

#the body of the class is executed using dict from above as local 
# namespace 
exec(class_body, globals(), class_dict)
Foo = type(class_name, class_parents, class_dict)

# viewing the class dict reveals the name bindings from class body
print(class_dict)
foo = Foo('tsemach')
foo.print()
