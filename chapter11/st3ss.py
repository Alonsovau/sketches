from socketserver import ThreadingUDPServer, BaseRequestHandler


class TimeHandler(BaseRequestHandler):
    def handle(self):
        pass


if __name__ == '__main__':
    serv = ThreadingUDPServer(('', 20000), TimeHandler)
    serv.serve_forever()


from socket import socket, AF_INET, SOCK_DGRAM
import time


def time_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    socket.bind(address)
    while True:
        msg, addr = sock.recvfrom(8192)
        print('Got message from ', addr)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), addr)


if __name__ == '__main__':
    time_server(('', 20000))
# 直接使用socket来建立UDP服务器
