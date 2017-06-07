# 使用延迟计算属性
# 想将一个只读属性定义成一个 property，并且只在访问的时候才会计算结果。但是一旦被访问后，你希望结果值被缓存起来，不用每次都去计算。


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            print(self.func.__name__)
            print(instance)
            setattr(instance, self.func.__name__, value)
            return value

    def __delete__(self, instance):
        del instance.__dict__[self.func.__name__]

    def __set__(self, instance, value):
        instance.__dict__[self.func.__name__] = value


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(4.0)
print(c.radius)
print(c.area)
print(c.area)
print(c.perimeter)
print(c.perimeter)


cc = Circle(5.0)
print(vars(cc))
print(cc.area)
print(vars(cc))
print(cc.__dict__)
print(cc.area)
# del c.area
print('after del:', vars(cc))
print(cc.area)
print('--------')
cc.area = 25
print(cc.area)


def lazyproperty2(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy


class Circle2:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty2
    def area(self):
        print('c2: computing area')
        return math.pi * self.radius ** 2

    @lazyproperty2
    def perimeter(self):
        print('c2: computing perimeter')
        return 2 * math.pi * self.radius


c2 = Circle2(4.0)
print('c2:', c2.area)
print('c2:', c2.area)
try:
    c2.area = 23
except Exception as e:
    print('Exception:', e)
