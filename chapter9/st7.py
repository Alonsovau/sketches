# 利用装饰器强制函数上的类型检查
from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func
        # 如果全局变量__debug__被设置成了False(当你使用-O或-OO参数的优化模式执行程序时)，那么就直接返回未修改过的函数本身

        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)


spam(1, 2, 3)
spam(1, 'hello', 3)
# spam(1, 'hello', 'world')


@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
print(bar(2))
# 它对于有默认值的参数并不适用
# print(bar(2, 3))
print(bar(4, [1, 2, 3]))