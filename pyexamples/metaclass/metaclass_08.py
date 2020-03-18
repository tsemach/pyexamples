"""
<description>
                                                                    
</description>

<output>
Traceback (most recent call last):
  File "metaclass_08.py", line 7, in <module>
    o = Conn.init()
AttributeError: type object 'Conn' has no attribute 'init'                                            
</output>
"""
class Conn(object):

    def __init__(self):
        raise RuntimeError("Conn must creating by the pool")

o = Conn.init()
print(o.l)
