from multiprocessing.connection import Client
from multiprocessing.reduction import recv_handle
import os, sys
from socket import socket, AF_INET, SOCK_STREAM


def worker(server_address):
    serv = Client(server_address, authkey=b'peekaboo')
    serv.send(os.getpid())
    while True:
        fd = recv_handle(serv)
        print('WORKER: GOT FD', fd)
        with socket(AF_INET, SOCK_STREAM, fileno=fd) as client:
            while True:
                msg = client.recv(1024)
                if not msg:
                    break
                print('WORKER: RECV {!r}'.format(msg))
                client.send(msg)
# 要运行工作者，执行执行命令python3 workermp.py /tmp/servconn效果跟使用 Pipe()例子是完全一样的。文件描述符的传递会涉及到UNIX域套接字的创建和套接字的sendmsg()方法。不过这种技术并不常见


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: worker.py server_address', file=sys.stderr)
        raise SystemExit(1)
    worker((sys.argv[1]))
