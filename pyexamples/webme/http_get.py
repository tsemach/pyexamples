from engine import Engine as engine


class HttpGet(object):
    def __init__(self, path):
        self._path = path
        self._http_get = None

    @property
    def path(self):
        return self._path

    def __call__(self, fn):
        print("HttpGet:__call__ is called, path is {}".format(self._path))
        print(type(fn))
        self._http_get = fn
        engine().add_http_get(self)

    def run(self, path):
        print(f"Httpget:run() path = {path}")
        print("HttpGet:run() is called with path = {}".format(self._path))
        self._http_get(self._path)

