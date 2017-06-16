# 将装饰器定义为类
import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


print(add(2, 3))
print(add(4, 5))
print(add.ncalls)
s = Spam()
s.bar(1)
s.bar(2)
s.bar(3)
print(s.bar.ncalls)
print(Spam.bar.ncalls)


s = Spam()
def grok(self, x):
    pass


print(grok.__get__(s, Spam))


def profiled2(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda : ncalls
    return wrapper


@profiled2
def add(x, y):
    return x + y


print(add(2, 3))
print(add(3, 3))
print(add.ncalls())
# 对于ncalls的访问现在是通过一个被绑定为属性的函数来实现
