# 解除一个装饰器
from functools import wraps


def somedecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass
    return wrapper


@somedecorator
def add(x, y):
    return x + y


orig_add = add.__wrapped__
print(orig_add(5, 6))


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


print(add(2, 3))
print(add.__wrapped__.__wrapped__(2, 3))
# 并不是所有的装饰器都使用了@wraps
# 因此这里的方案并不全部适用
# 特别的内置的装饰器@staticmethod和@classmethod就没有遵循这个约定
# 它们把原始函数存储在属性__func__中
