# 在不同的python解释器之间交互
from multiprocessing.connection import Listener
import traceback


def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')


def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()


echo_server(('', 25000), authkey=b'peekaboo')
# 和socket不同，所有对象会通过pickle序列化，任何兼容pickle的对象都能在此连接上被发送和接受


s = Listener('/tmp/myconn', authkey=b'peekaboo')
# 使用unix域套接字
s = Listener(r'\\.\pipe\myconn', authkey=b'peekaboo')
# 使用windows命名管道来创建
