import os
from asynproc import Process
myProc = Process("myprogram.app")

while True:
    # check to see if process has ended
    poll = myProc.wait(os.WNOHANG)
    if poll is not None:
        break
    # print any new output
    out = myProc.read()
    if out != "":
        print(out)