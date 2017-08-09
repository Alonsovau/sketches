# 定义一个Actor任务
from queue import Queue
from threading import Thread, Event


class ActorExit(Exception):
    pass


class Actor:
    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        while True:
            msg = self.recv()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('Got: ', msg)


p = PrintActor()
p.start()
p.send('Hello')
p.send('World')
p.close()
p.join()


# 放宽异步同步消息发送要求可以使用生成器简化定义
def print_actor():
    while True:
        try:
            msg = yield
            print('Got: ', msg)
        except GeneratorExit:
            print('Actor terminating')


pp = print_actor()
next(pp)
pp.send('Hello')
pp.send('World')


class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self, 'do_'+tag)(*payload)

    def do_A(self, x):
        print('Running A', x)

    def do_B(self, x, y):
        print('Running B', x, y)


a = TaggedActor()
a.start()
a.send(('A', 1))
a.send(('B', 2, 3))
a.close()
a.join()
