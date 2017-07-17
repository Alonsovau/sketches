# 实现远程方法调用
import pickle
from multiprocessing.connection import Listener
from threading import Thread
import json


class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                func_name, args, kwargs = pickle.loads(connection.recv())
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass


class RPCHandler2:
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                func_name, args, kwargs = json.loads(connection.recv())
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(json.dumps(r))
                except Exception as e:
                    connection.send(json.dumps(str(e)))
        except EOFError:
            pass


def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)

handler2 = RPCHandler2()
handler2.register_function(add)
handler2.register_function(sub)

rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')
rpc_server(handler2, ('localhost', 18000), authkey=b'peekaboo')
