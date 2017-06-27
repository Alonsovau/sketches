# 在类上强制使用编程规约
from inspect import signature
import logging


class Mymeta(type):
    def __new__(cls, clsname, bases, clsdict):
        # clsname is name of class being define
        # bases is tuple of base classes
        # clsdict is class dictionary
        return super().__new__(cls, clsname, bases, clsdict)


# 或者
class MyMeta2(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)


class Root(metaclass=Mymeta):
    pass


class A(Root):
    pass


class B(Root):
    pass


class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: '+name)
        return super().__new__(cls, clsname, bases, clsdict)
# 拒绝任何有混合大小写作为方法的类定义


class Root(metaclass=NoMixedCaseMeta):
    pass


class A(Root):
    def foo_bar(self):
        pass


# class B(Root):
#     def fooBar(self):
#         pass


class MatchSignaturesMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            prev_dfn = getattr(sup, name, None)
            if prev_dfn:
                pre_sig = signature(prev_dfn)
                val_sig = signature(value)
                if pre_sig != val_sig:
                    logging.warning('Signature mismatch in %s. %s != %s',
                                    value.__qualname__, pre_sig, val_sig)
# 检测重载方法，确保它的调用参数和父类中原始方法有着相同的参数签名


class Root(metaclass=MatchSignaturesMeta):
    pass


class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass


class B(A):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass