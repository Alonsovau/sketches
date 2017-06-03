from socketserver import StreamRequestHandler, TCPServer
from functools import partial


class EchoHandler(StreamRequestHandler):
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super.__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack +line)

# serv = TCPServer(('', 15000), EchoHandler)
serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVE:'))
# serv = TCPServer(('', 15000), lambda *args, **kwargs: EchoHandler(*args, ack=b'RECEIVED:', **kwargs)) #等价
serv.serve_forever()
