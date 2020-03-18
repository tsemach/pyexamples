import threading
import time

"""
<description>
from: https://pymotw.com/3/threading/

Each Thread instance has a name with a default value that can be changed as the thread is created. Naming threads 
is useful in server processes with multiple service threads handling different operations.
</description>
<output>
worker Starting
Thread-1 Starting
my_service Starting
worker Exiting
Thread-1 Exiting
my_service Exiting
</output>
"""


def worker():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(0.2)
    print(threading.current_thread().getName(), 'Exiting')


def my_service():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(0.6)
    print(threading.current_thread().getName(), 'Exiting')


t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)  # use default name

w.start()
w2.start()
t.start()
