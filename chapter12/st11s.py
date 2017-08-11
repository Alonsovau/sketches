# 防止忘记detach，使用上下文管理器协议
from contextlib import contextmanager
from collections import defaultdict


class Exchange:
    def __init__(self):
        self._subscribes = set()

    def attach(self, task):
        self._subscribes.add(task)

    def detach(self, task):
        self._subscribes.remove(task)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    def send(self, msg):
        for subscribe in self._subscribes:
            subscribe.send(msg)


_exchanges = defaultdict(Exchange)


def get_exchange(name):
    return _exchanges[name]


class Task:
    def send(self, msg):
        print(msg)


task_a = Task()
task_b = Task()


exc = get_exchange('name')
with exc.subscribe(task_b, task_b):
    exc.send('msg1')
    exc.send('msg2')
