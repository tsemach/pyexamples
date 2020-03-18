"""
setattr example:

1) __setattr__: call on EVERY attribute assignment
2) if you implement __setattr__ you override the default
   assignment, make sure to add the key, value to dictionary
3) avoiding infinity loop by:
   super(Printer, self).__setattr__(key, value)
"""


class Printer(object):
    def __init__(self, msg=""):
        print("Printer:__init__: start")
        self._msg = msg
        print("Printer:__init__: end")

    def print(self):
        print("Printer:print: {}".format(self._msg))

    def __setattr__(self, key, value):
        print("Printer:__setattr__: key = %s, value = %s" % (key, value))
        super(Printer, self).__setattr__(key, value)


p = Printer("print me")
p.print()
