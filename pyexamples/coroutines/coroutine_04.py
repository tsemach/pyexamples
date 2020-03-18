def coro():
    print("coro: before hello")
    hello = yield "Hello"
    yield hello


c = coro()
print(next(c))
print("main: before send")
print(c.send("World"))
