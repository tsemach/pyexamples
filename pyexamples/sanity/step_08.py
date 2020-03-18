import importlib
from step_05 import SanityBase

if __name__ == "__main__":
    importlib.import_module("step_06")
    SanityBase.init()
    s = SanityBase.create("size")
    s.prepare(1024)
    s.run()
