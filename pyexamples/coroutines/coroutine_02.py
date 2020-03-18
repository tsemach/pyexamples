
"""
<description>
This example show how to methods can communicate by using next and send of the corouting.
line 15 - s = (yield) - makes match method corouting.
Note the yield is on the *right* side of the equation.
while match execute this line it keep its state and wait in someone will *send* him some value.
</description>

<output>
run() - is start
match() - === begin ===
match() - looking for pattern - tsemach
match() - before (yeird)
run() - after call to m.__next__
run() - going to send "this is tsemach" to m
match() - after (yeird)
match() - got from run <this is tsemach>
match() - before (yeird)
run() - going to send "more of tsemach" to m
match() - after (yeird)
match() - got from run <more of tsemach>
match() - before (yeird)
match() - === done ===
</output>
"""

def match(pattern):
    print("match() - === begin ===")
    print("match() - looking for pattern - " + pattern)
    try:
        while True:
            print("match() - before (yeird)")
            s = (yield)
            print("match() - after (yeird)")
            if pattern in s:
                print("match() - got from run <" + s + ">")
    except GeneratorExit:
        print("match() - === done ===")

def run():
    print("run() - is start")
    m = match("tsemach")
    m.__next__()
    print("run() - after call to m.__next__")
    print("run() - going to send \"this is tsemach\" to m")
    m.send("this is tsemach")
    print("run() - going to send \"more of tsemach\" to m")
    m.send("more of tsemach")
    m.close()


if __name__ == "__main__":
    run()
