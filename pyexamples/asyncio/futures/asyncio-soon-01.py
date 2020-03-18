import asyncio
import functools

def event_handler(loop, stop=False):
    print("event_handler() - event handler called")
    if loop:
        print("event_handler() - stopping the loop")
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.call_soon(functools.partial(event_handler, loop))
        loop.call_soon(functools.partial(event_handler, loop, stop=True))

        print("main() - starting the event loop")
        loop.run_forever()
    finally:
        print("main() - closing the event loop")
        loop.close()

