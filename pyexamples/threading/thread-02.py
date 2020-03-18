import threading

"""
<description>
from: https://pymotw.com/3/threading/

This example passes a number, which the thread then prints.
</description>
<output>
Worker: 0
Worker: 1
Worker: 2
Worker: 3
Worker: 4
</output>
"""


def worker(num):
    """thread worker function"""
    print('Worker: %s' % num)


for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
