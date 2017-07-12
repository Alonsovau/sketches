from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from ', self.client_address)
        for line in self.rfile:
            self.wfile.write(line)


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
# 使用StreamRequestHandler


from socketserver import ThreadingTCPServer, ForkingTCPServer


if __name__ == '__main__':
    serv = ThreadingTCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
# fork或者线程服务器潜在问题是会为每个客户端连接创建一个新的进程或者线程


if __name__ == '__main__':
    from threading import Thread
    NWORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler)
    for i in range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    serv.serve_forever()
# 先创建一个普通的非线程服务器，然后在一个线程池中使用serve_forever()方法来启动


if __name__ == '__main__':
    import socket
    serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
    serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    serv.server_bind()
    serv.server_activate()
    serv.serve_forever()
# 调整socket


if __name__ == '__main__':
    TCPServer.allow_reuse_address = True
    serv = TCPServer(('', 200000), EchoHandler)
    serv.serve_forever()


import socket


class EchoHandler(StreamRequestHandler):
    timeout = 5
    rbufsize = -1
    wbufsize = 0
    disable_nagle_algorithm = False

    def handle(self):
        print('Got connection from ', self.client_address)
        try:
            for line in self.rfile:
                self.wfile.write(line)
        except socket.timeout:
            print('Time out!')
# StreamRequestHandler更加灵活


from socket import socket, AF_INET, SOCK_STREAM


def echo_handler(address, client_sock):
    print('Got connection from {}'.format(address))
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)
    client_sock.close()


def echo_server(address, backlog = 5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = socket.accept()
        echo_handler(client_addr, client_sock)


if __name__ == '__main__':
    echo_server(('', 20000))
# 直接使用socket库来实现服务器
