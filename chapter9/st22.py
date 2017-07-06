# 定义上下文管理器的简单方法
import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


with timethis('counting'):
    n = 1000000
    while n > 0:
        n -= 1


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


items = [1, 2, 3]
with list_transaction(items) as working:
    working.append(4)
    working.append(5)
print(items)

try:
    with list_transaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError('oops')
except RuntimeError:
    pass
print(items)


class ctimethis:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))
# 通常上下文管理器需要定义一个类，实现enter,exit方法，@contextmanager仅仅包含上下文管理函数
# 文件、网络连接、锁等对象需要支持with，需要单独实现enter、exit方法