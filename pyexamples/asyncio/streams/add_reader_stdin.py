import asyncio
import sys

"""
from: https://stackoverflow.com/questions/25351999/what-file-descriptor-object-does-python-asyncios-loop-add-reader-expect

Add watch file descriptor, This will echo stuff writen on stdin.
"""


def file_callback(*args):
    print("Received: " + sys.stdin.readline())

loop = asyncio.get_event_loop()
task = loop.add_reader(sys.stdin.fileno(), file_callback)
loop.run_forever()
