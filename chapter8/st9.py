# 创建新的类或实例属性
# 创建一个新的拥有一些额外功能的实例属性类型，比如类型检查


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
print(p.x)
# calls Point.x.__get__(p, Point)
print(Point.x)
# calls Point.x.__get__(None, Point)


class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate


@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


stock = Stock('oo', 0, 8.9)
print(stock.name, stock.price, stock.shares)

