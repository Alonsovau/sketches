# 简化数据结构的初始化
import math


class Structure1:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


class Point(Structure1):
    _fields = ['x', 'y']


class Circle(Structure1):
    _fields = ['radius']


    def area(self):
        return math.pi * self.radius ** 2


s = Stock('ACME', 50, 91.1)
p = Point(2, 3)
c = Circle(4.5)
# s2 = Stock('')


# 支持关键字参数
class Structure2:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Invaild argument(s): {}'.format(','.join(kwargs)))


class Stock2(Structure2):
    _fields = ['name', 'shares', 'price']


s1 = Stock2('ACME', 50, 91.1)
s2 = Stock2('ACME', 50, price=91.1)
# s3 = Stock2('ACME', 50, price=91.1, aa=1)


class Structure3:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))


class Stock3(Structure3):
    _fields = ['name', 'shares', 'price']


s1 = Stock3('ACME', 50, 90.1)
s2 = Stock3('ACME', 50, 90.1, date='8/2/2012')


class Structure: # Class variable that specifies expected
    _fields= []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
# Set the arguments (alternate)
        self.__dict__.update(zip(self._fields,args))
# 尽管这也可以正常工作，但是当定义子类的时候问题就来了。当一个子类定义了 slots 或者通过 property(或描述器) 来包装某个属性，那么直接访问实例字典就不 起作用了。我们上面使用 setattr() 会显得更通用些，因为它也适用于子类情况。 这种方法唯一不好的地方就是对某些 IDE 而已，在显示帮助函数时可能不太友好。




