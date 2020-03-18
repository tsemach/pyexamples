
class Connection(object):
    def __init__(self, ip="172.23.0.1"):
        self.ip = ip

    def set_ip(self, ip):
        if not ip.startswith("172.23"):
            raise ValueError("ip not start with 172.23")
        self._ip = ip

    def get_ip(self):
        return self._ip

    def __srt__(self):
        return self.ip

    ip = property(get_ip, set_ip)


conn = Connection("172.23.0.1")
print(conn.ip)

more = Connection("172.23.0.2")
print(more.ip)
print(conn.ip)
print(hex(id(more.ip)))
print(hex(id(conn.ip)))
