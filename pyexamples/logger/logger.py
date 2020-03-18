
import logging.config
import yaml
# import pprint

"""
from: 

Output to file as well as to console
"""


class Logger(object):
    loggers = {}

    def __init__(self):
        pass

    @staticmethod
    def init():
        with open("logger-02.yml", 'r') as logging_conf_file:
            names = []
            config_dict = yaml.load(logging_conf_file)
            for logger in config_dict['loggers']:
                names.append(logger)
            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(config_dict)

        logging.config.dictConfig(config_dict)
        for name in names:
            Logger.loggers[name] = logging.getLogger(name)

    @staticmethod
    def get(name):
        logger = logging.getLogger(name)
        Logger.loggers[name] = logger
        return logger

    @staticmethod
    def set_level(name, level):
        logger = Logger.loggers[name]
        logger.setLevel(level)
