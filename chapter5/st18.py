# 将文件描述符包装成文件对象
# 看不懂
from socket import socket, AF_INET, SOCK_STREAM
def echo_client(client_sock, addr):
    print('Got connection from', addr)
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1', closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1', closefd=False)
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()


def echo_server(adress):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(adress)
    socket.listen(1)
    while True:
        client, addr = socket.accept()
        echo_client(client, addr)
# 需要重点强调的一点是，上面的例子仅仅是为了演示内置的open()函数的一个特性，并且也只适用于基于Unix的系统。
# 如果你想将一个类文件接口作用在一个套接字并希望你的代码可以跨平台，请使用套接字对象的makefile()方法。
# 但是如果不考虑可移植性的话，那上面的解决方案会比使用makefile()性能更好一点。