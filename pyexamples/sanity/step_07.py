from step_05 import SanityBase
from step_06 import SanitySize


if __name__ == "__main__":
    SanityBase.init()
    s = SanityBase.create("size")
    s.prepare(1024)
    s.run()
