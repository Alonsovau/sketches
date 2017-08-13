# 使用生成器来实现一个并发网络应用程序
from collections import deque
from select import select


class YieldEvent:
    def handle_yield(self, sched, task):
        pass

    def handle_resume(self, sche, task):
        pass


class Scheduler:
    def __init__(self):
        self._numtasks = 0
        self._ready = deque()
        self._read_waiting = {}
        self._write_waiting = {}

    def _iopoll(self):
        rset, wset, eset = select(self._read_waiting, self._write_waiting, [])
        for r in rset:
            evt, task = self._read_waiting.pop(r)
            evt.handle_resume(self, task)
        for w in wset:
            evt, task = self._write_waiting.pop(w)
            evt.handle_resume(self, task)

    def new(self, task):
        self._ready.append((task, None))
        self._numtasks += 1

    def add_ready(self, task, msg=None):
        self._ready.append((task, msg))

    def _write_wait(self, fileno, evt, task):
        self._write_waiting[fileno] = (evt, task)

    def _read_wait(self, fileno, evt, task):
        self._read_waiting[fileno] = (evt, task)

    def run(self):
        while self._numtasks:
            if not self._ready:
                self._iopoll()
            task, msg = self._ready.popleft()
            try:
                r = task.send(msg)
                if isinstance(r, YieldEvent):
                    r.handle_yield(self, task)
                else:
                    raise RuntimeError('unrecognized yield event')
            except StopIteration:
                self._numtasks -= 1
