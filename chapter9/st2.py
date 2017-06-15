# 创建装饰器时保留函数元信息
import time
from functools import wraps
from inspect import signature


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@timethis
def countdown(n: int):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1


countdown(10000000)
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)
# 没有@wraps也可以使用，但是丢失了所有有用的信息

print(countdown.__wrapped__(1000000))
# 直接通过属性访问被包装函数

print('__wrapped__属性还能正确暴露底层参数签名信息')
print(signature(countdown))