from multiprocessing.connection import Listener
from multiprocessing.reduction import send_handle
import socket, sys


def server(work_address, port):
    work_serv = Listener(work_address, authkey=b'peekaboo')
    worker = work_serv.accept()
    worker_pid = worker.recv()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(('', port))
    s.listen(1)
    while True:
        client, addr = s.accept()
        print('SERVER: Got connection from ', addr)
        send_handle(worker, client.fileno(), worker_pid)
        client.close()
# 运行这个服务器：python3 st11s.py /tmp/servconn 15000

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: server.py server_port port', file=sys.stderr)
        raise SystemExit(1)
    server(sys.argv[1], int(sys.argv[2]))