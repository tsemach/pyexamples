"""
<description>
                                                                                                   
</description>

<output>
main: dir of global is ['Loop', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'level1', 'loop']
main: loop address is 0x7fafe6e3dcc0
level1: enter to .. loop - 0
level1: loop address is 0x7fafe6e3dcc0
level1: loop address is 0x7fafe6e3dcc0
level1: dir is - ['loop']
level1: loop is <1>
level2: loop address is 0x7fafe6e3dcc0
level2: loop is - 1
level2: more address is 0x7fafe6e3dcc0
level2: more is - 2
main: loop is 2
</output>
"""


loop = None


class Loop(object):
    def __init__(self, n):
        self._me = n

    def __str__(self):
        return str(self._me)


def level1(loop):
    print(f'level1: enter to .. loop - {loop}')
    print(f'level1: loop address is {hex(id(loop))}')
    loop._me = 1
    print(f'level1: loop address is {hex(id(loop))}')
    print(f'level1: dir is - {dir()}')
    print(f'level1: loop is <{loop}>')

    def level2(more):
        print(f'level2: loop address is {hex(id(loop))}')
        print(f'level2: loop is - {loop}')
        more._me = 2
        print(f'level2: more address is {hex(id(more))}')
        print(f'level2: more is - {more}')

    level2(loop)

loop = Loop(0)
print(f'main: dir of global is {dir()}')
print(f'main: loop address is {hex(id(loop))}')
level1(loop)
print(f'main: loop is {loop}')
