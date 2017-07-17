from multiprocessing.connection import Client
from multiprocessing.reduction import recv_handle
import os, sys
from socket import socket, AF_INET, SOCK_STREAM
import socket as SOCKET
import struct


def recv_fd(sock):
    msg, ancdata, flags, addr = sock.recvmsg(1, SOCKET.CMSG_LEN(struct.calcsize('i')))
    cmsg_level, cmsg_type, cmsg_data = ancdata[0]
    assert cmsg_level == SOCKET.SOL_SOCKET and cmsg_type == SOCKET.SCM_RIGHTS


def worker2(server_address):
    serv = socket(SOCKET.AF_UNIX, SOCKET.SOCK_STREAM)
    serv.connect(server_address)
    while True:
        fd = recv_fd(serv)
        print('WORKER: Got FD', fd)
        with socket(SOCKET.AF_INET, SOCKET.SOCK_STREAM, fileno=fd) as client:
            while True:
                msg = client.recv(1024)
                if not msg:
                    break
                print('WORKER: RECV {!r}'.format(msg))
                client.send(msg)


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
    # worker((sys.argv[1]))
    worker(sys.argv[1])
