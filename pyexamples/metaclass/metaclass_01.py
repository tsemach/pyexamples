"""
<description>
from: http://masnun.com/2016/05/03/python-metaclass-explained.html

Create class with metaclass type.                                                               
The below code is equivalent to:
class MyClass(int):
    name = "MyClass" 
</description>

<output>
<class '__main__.MyClass'>
</output>
"""


MyClass = type('MyClass', (), {})

instance = MyClass()
print(type(instance))

