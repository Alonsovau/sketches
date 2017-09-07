# bash:time python3 someprogram.py
# 使用Unix时间函数
# bash:python3 -m cProfile someprogram.py
import time
from functools import wraps
from contextlib import contextmanager
from timeit import timeit


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(1000000)


@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} : {}'.format(label, end - start))


with timeblock('counting'):
    n = 100000
    while n > 0:
        n -= 1


print(timeit('math.sqrt(2)', 'import math'))
print(timeit('sqrt(2)', 'from math import sqrt', number=1000))
# 测试小的代码片段运行性能，使用timeit
# timeit会执行第一个参数中语句100w次并计算运行时间，第二个是运行之前的配置环境
# 想改变循环执行次数，设置number参数


# 执行性能测试时，获取的结果都是近似值
# time.perf_counter()函数会在给定平台上获取最高精度
# 但是他仍基于时钟时间，很多因素影响精度，比如机器负载


def timethis2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        r = func(*args, **kwargs)
        end = time.process_time()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper
# 使用time.process_time()代替


@timethis2
def countdown2(n):
    while n > 0:
        n -= 1


countdown2(1000000)
