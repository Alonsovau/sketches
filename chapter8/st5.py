# 在类中封装属性名
class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass
# _开头应该是内部实现


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()
# 使用双下划线开始会导致访问名称变成其他形式，比如私有属性会被分别重命名为_B__private和_B__private_method
# 目的是继承，这种属性通过继承是无法被覆盖的


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 # 不会覆盖B.__private

    def __private_method(self):
        pass
# 不会覆盖B.__private_method()
# 这里被重命名为_C_private和_C_private_method

lambda_ = 0
# 关键字冲突，用_作为后缀
