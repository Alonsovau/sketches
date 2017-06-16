# 将装饰器定义为类的一部分
from functools import wraps


class A:
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper


a = A()


# an instance method
@a.decorator1
def spam():
    pass


# a class method
@A.decorator2
def grok():
    pass


class B(A):
    @A.decorator2
    def bar(self):
        pass
# 装饰器要被定义成类方法并且你必须显式的使用父类名去调用它。你不能使用@B.decorator2，因为在方法定义时，这个类B还没有被创建

