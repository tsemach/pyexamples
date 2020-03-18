from aiohttp import web


async def hello(request):
    return web.Response(text="Hello, world")


class more(object):
    def __init__(self):
        pass

    @staticmethod
    def sayhi(request):
        return web.Response(text="from more.sayhi")

    def __call__(self, request):
        return web.Response(text="From class more __call__")


app = web.Application()
app.router.add_get('/', hello)
app.router.add_get('/class', more())
app.router.add_get('/sayhi', more.sayhi)

web.run_app(app)
