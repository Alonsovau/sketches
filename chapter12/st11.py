from collections import defaultdict


class Exchange:
    def __init__(self):
        self._subscribes = set()

    def attach(self, task):
        self._subscribes.add(task)

    def detach(self, task):
        self._subscribes.remove(task)

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
exc.attach(task_a)
exc.attach(task_b)
exc.send('msg1')
exc.send('msg2')
exc.detach(task_a)
exc.detach(task_b)
