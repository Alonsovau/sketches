# 调用父类方法
class A:
    def __init__(self):
        self.x = 0

    def spam(self):
        print('A.spam')


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1

    def spam(self):
        print('B.spam')
        super().spam()


b = B()
b.spam()


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, key, value):
        if key.startwith('_'):
            super().__setattr__(key, value)
        else:
            setattr(self._obj, key, value)
# 在上面代码中， setattr () 的实现包含一个名字检查。如果某个属性名以下划线开头，就通过 super() 调用原始的 setattr () ，否则的话就委派给内部的代 理对象 self. obj 去处理。这看上去有点意思，因为就算没有显式的指明某个类的父 类， super() 仍然可以有效的工作。


class Base:
    def __init__(self):
        print('Base.__init__')


class AA(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')


class BB(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')


class CC(AA, BB):
    def __init__(self):
        AA.__init__(self)
        BB.__init__(self)
        print('C.__init__')


cc = CC()
print(CC.__mro__)
# Base.__init__()被调用2次，应全部使用super()调用


class AAA:
    def spam(self):
        print('AAA.spam')
        super().spam()


# aaa = AAA()
# aaa.spam()
class BBB:
    def spam(self):
        print('BBB.spam')


class CCC(AAA, BBB):
    pass


ccc = CCC()
ccc.spam()
# AAA中调用的是BBB中的spam()方法
print(CCC.__mro__)
