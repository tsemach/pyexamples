import logging
from logger import Logger

# logger_a_doit = logging.getLogger("module_a.doit")
# logger_a_more = logging.getLogger("module_a.more")

logger_a_doit = Logger.get("module_a.doit")
logger_a_more = Logger.get("module_a.more")


class ModuleA(object):
    def __init__(self):
        class NoParsingFilter(logging.Filter):
            def filter(self, record):
                print("IN FILTER {}".format(record.getMessage()))
                return record.getMessage().startswith('[doit]')

        logger_a_doit.addFilter(NoParsingFilter())

        pass

    def doit(self):
        logger_a_doit.info("[doit]: INFO I am module-a.doit")
        logger_a_doit.debug("[doit]: DEBUG hey, I am module-a.doit")

    def more(self):
        logger_a_more.info("INFO hey, I am module-a.doit")
        logger_a_more.debug("DEBUG hey, I am module-a.doit")

    def stam(self):
        logger_a_doit.info("[doit]: INFO hey, I am module-a.doit")
        logger_a_doit.debug("[doit]: DEBUG hey, I am module-a.doit")