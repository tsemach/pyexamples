
import logging.config
import yaml

"""
from: 

Output to file as well as to console
"""

with open("logger-02.yml", 'r') as logging_conf_file:
    config_dict = yaml.load(logging_conf_file)

logging.config.dictConfig(config_dict)

logger = logging.getLogger("logger-02")

logger.info('Hey, this is working!')
logger.debug('Hey, this is working too!')


