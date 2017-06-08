# 实现数据模型的类型约束
# 你想定义某些在属性赋值上面有限制的数据结构


class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >=0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


class Stock:
    name = SizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.price = price
        self.shares = shares


s = Stock('ACME', 9, 90.1)
print(s.name)
s.shares = 75
# s.shares = -10
# s.price = 'a lot'
# s.name = 'ALALALAL'


def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate


@check_attributes(name=SizedString(size=8), shares=UnsignedInteger, price=UnsignedFloat)
class Stock2:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s2 = Stock2('ACME', 90, 90.1)
print(s2.price)
# s2.price = ''
# s2.shares = -90
# 类装饰器方式实现


class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)


class Stock3(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s3 = Stock3('oo', 90, 90.9)
print(s3.shares)
# s3.price = '90'
# 使用元类实现
