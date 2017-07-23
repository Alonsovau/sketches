# 判断线程是否已经启动
from threading import Thread, Event, Condition
import time


def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)


# start_evt = Event()
# t = Thread(target=countdown, args=(10, start_evt))
# t.start()
# start_evt.wait()
# print('countdown is running')


class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = Condition()

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        while True:
            time.sleep(self._interval)
            while self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag:
                self._cv.wait()


ptimer = PeriodicTimer(5)
ptimer.start()


def countdown2(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1


def countup(last):
    n = 0
    while n <last:
        ptimer.wait_for_tick()
        print('counting', n)
        n += 1


Thread(target=countdown2, args=(10,)).start()
Thread(target=countup, args=(5,)).start()