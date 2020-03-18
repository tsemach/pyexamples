
import logging.config
from logger import Logger
from module_a import ModuleA
from module_b import ModuleB

"""
from: 

Output to file as well as to console
"""

if __name__ == "__main__":
    Logger.init()

    logger = Logger.get("main")
    # logger = logging.getLogger("main")

    logger.info('[main] Hey, this is working!')
    logger.debug('[main] Hey, this is working too!')

    module_a = ModuleA()
    module_b = ModuleB()

    logger.info("going to print module-a")
    module_a.doit()
    module_a.stam()
    module_a.more()

    logger.info("going to print module-b")
    module_b.doit()
    module_b.more()

    logger.info("after set level DEBUG of module-b")
    Logger.set_level("module_b.more", logging.DEBUG)
    module_b.doit()
    module_b.more()



