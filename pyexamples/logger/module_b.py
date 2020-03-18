from logger import Logger

# logger = logging.getLogger("module-b")
logger_b_doit = Logger.get("module_b.doit")
logger_b_more = Logger.get("module_b.more")

class ModuleB(object):
    def __init__(self):
        pass

    def doit(self):
        logger_b_doit.info("INFO hey, I am module-b")
        logger_b_doit.debug("hey, I am module-b")

    def more(self):
        logger_b_more.info("INFO hey, I am module-b")
        logger_b_more.debug("hey, I am module-b")
