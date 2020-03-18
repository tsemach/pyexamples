"""
<description>
                                                                                                    
</description>
<output>
main: dir of global is <['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'level1', 'loop']>
main: loop address is <0x7f3923151e30>


level1: enter to .. loop - <loop on global>
level1: loop address is <0x7f3923151e30>
level1: dir is - <['loop']>
level1: loop address is <0x7f3923151db0>
level1: dir is - <['loop']>
level1: loop is <in level1>


level2: loop address is <0x7f3923151db0>
level2: loop is - <in level1>
level2: more address is <0x7f3923151df0>
level2: more is - <in level2>
level2: dir is <['loop', 'more']>


main: loop is <loop on global>
</output>
"""

loop = None


def level1(loop):
    print('\n')
    print(f'level1: enter to .. loop - <{loop}>')
    print(f'level1: loop address is <{hex(id(loop))}>')
    print(f'level1: dir is - <{dir()}>')
    loop = "in level1"
    print(f'level1: loop address is <{hex(id(loop))}>')
    print(f'level1: dir is - <{dir()}>')
    print(f'level1: loop is <{loop}>')

    def level2(more):
        print('\n')
        print(f'level2: loop address is <{hex(id(loop))}>')
        print(f'level2: loop is - <{loop}>')
        more = "in level2"
        print(f'level2: more address is <{hex(id(more))}>')
        print(f'level2: more is - <{more}>')
        print(f'level2: dir is <{dir()}>')

    level2(loop)

loop = "loop on global"
print('\n')
print(f'main: dir of global is <{dir()}>')
print(f'main: loop address is <{hex(id(loop))}>')
level1(loop)
print('\n')
print(f'main: loop is <{loop}>')
