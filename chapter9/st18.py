# 以编程方式定义类
import types, abc


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost,
}

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__
s = Stock('ACME', 50, 91.1)
print(s)
print(s.cost())

Stock2 = types.new_class('Stock2', (), {'metaclass': abc.ABCMeta}, lambda ns: ns.update(cls_dict))
print(Stock2)
print(type(Stock2))
# 创建的类需要一个不同的元类


class Spam(Base, debug=True, typecheck=False):
    pass

Spam = types.new_class('Spam', (Base,),
                       {'debug': True, 'typecheck': False},
                       lambda ns: ns.update(cls_dict))
