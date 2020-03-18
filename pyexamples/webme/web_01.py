from datetime import datetime
from http_get import HttpGet
from engine import Engine
#import aiojobs
from aiojobs.aiohttp import setup, spawn

engine = Engine()


@HttpGet('/app')
def wget(name):
    print("Hello {}, it is now: {}".format(name, datetime.now()))


engine.run()
