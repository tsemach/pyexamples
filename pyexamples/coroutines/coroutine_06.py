
def minimize():
    print("Start before yield")
    current = yield
    print("Start after yield, current = {}".format(current))
    while True:
        print("in while, before yield, current {}".format(current))
        value = yield current
        print("in while, before yield, value {}".format(value))
        current = min(value, current)

it = minimize()
print("main: before next")
next(it)
print("main: after next")
print(it.send(9))
print(it.send(4))
print(it.send(22))
print(it.send(8))
print(it.send(-1))
