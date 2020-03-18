import threading

"""
<description>
from: https://pymotw.com/3/threading/

The simplest way to use a Thread is to instantiate it with a target function and 
call start() to let it begin working.
</description>
<output>
Worker is working
Worker is working
Worker is working
Worker is working
Worker is working
</output>
"""
def worker():
    """thread worker function"""
    print('Worker is working')
    return

for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
