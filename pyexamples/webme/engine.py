from singleton import singleton


@singleton
class Engine(object):
    def __init__(self):
        self._cb = {}

    def add_http_get(self, o):
        print("going to add {} to {}".format(o.path, o))
        self._cb[o.path] = o
        print(self._cb['/app'])

    def run(self):
        o = self._cb['/app']
        print("o is {}".format(o))
        o.run('/app')

# if __name__ == "__main__":
