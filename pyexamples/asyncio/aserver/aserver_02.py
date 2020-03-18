from aiohttp import web


async def hello(request):
    return web.Response(text="Hello, world")


class MyView(web.View):
    async def get(self):
        return await web.get_resp(self.request)

    async def post(self):
        return await web.post_resp(self.request)


app = web.Application()
app.router.add_get('/', hello)
app.router.add_view('/view', MyView)

web.run_app(app)
