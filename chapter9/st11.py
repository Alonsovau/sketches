# 装饰器为被包装函数增加参数
from functools import wraps
import inspect


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)

spam(2, 3, 4)
spam(1, 2, 3, debug=True)
print(inspect.signature(spam))
# 签名并不对


def optional_debug1(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*func, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug', inspect.Parameter.KEYWORD_ONLY, default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper


@optional_debug1
def spam(a, b, c):
    print(a, b, c)


print(inspect.signature(spam))