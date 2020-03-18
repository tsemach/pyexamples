"""
<description>
Coroutine "hello world" example.

On start co = hello() doesn't run the method just now co is a reference to coroutine.
First next is call - this can the yield "Hello" to generate the value of "Hello".
So the return value next(co) is "Hello".
Second co.send("Word") cause the word "World" to *send* to hello() method.
This cause the local argument hello of hello method to get the value of "World".
Than hello method continue to next yield but because the send is also generate a next request
The value of "World" is return back as the return value of co.send("World")
</description>
<output>
Hello World
</output>
"""

def hello():
    hello = yield "Hello"
    yield hello

co = hello()
print(next(co) + " " + co.send("World"))
