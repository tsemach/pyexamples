import logging


"""
from: 

The format:
    levelname - DEBUG, INFO, WARNING, ERROR, CRITICAL ...
"""


def do_something():
    """wait for the condition and use the resource"""
    logging.debug("Starting my code")
    logging.debug("That's it")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(levelname)s %(message)s',
)

do_something()
