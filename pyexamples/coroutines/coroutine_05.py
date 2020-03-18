def match(pattern):
    print('Looking for ' + pattern)
    try:
        while True:
            s = (yield)
            if pattern in s:
                print(s)
    except GeneratorExit:
        print("=== Done ===")


m = match("coroutines")
next(m)
m.send("the coroutines lesson it confusing")
m.send("cant make need to sleep")
m.send("bu")
m.close()