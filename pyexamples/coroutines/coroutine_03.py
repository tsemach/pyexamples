"""
<description>
send parameter to conroutine                                                      
</description>
<output>
echo-0: start
main: next is -1
main: before for loop

main: loop is 0
echo-1: 0
main: send is 0

main: loop is 1
echo-2: 1
main: send is 1

main: loop is 2
last echo-3: 2
main: send is 2
</output>
"""
def echo():
    print("echo-0: start")
    i = yield -1
    print(f'echo-1: {i}')
    i = yield i
    print(f'echo-2: {i}')
    i = yield i
    print(f'last echo-3: {i}')
    yield i


co = echo()
print(f'main: next is {next(co)}')
print("main: before for loop")
for i in range(3):
    print('\n')
    print(f'main: loop is {i}')
    print(f'main: send is {co.send(i)}')
 
