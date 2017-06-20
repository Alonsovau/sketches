# 使用装饰器扩展类的功能
def log_getattribute(cls):
    orig_getattribute = classmethod.__getattribute__

    def new_getattribute(self, name):
        print('getting:', name)
        return orig_getattribute

    cls.__getattribute__ = new_getattribute
    return cls


@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


a = A(22)
a.x
a.spam


class LoggedGetattribute:
    def __getattribute__(self, name):
        print('Getting:', name)
        return super().__getattribute__(name)


class A(LoggedGetattribute):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


a = A(99)
a.x
a.spam
# 混入依赖super,不如装饰器快
