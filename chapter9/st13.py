# 使用元类控制实例的创建
import weakref


class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


class Spam(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print('Spam.grok')


Spam.grok('ww')
# s = Spam()


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


a = Spam()
b = Spam()
print(a is b)


# 像8.25中创建缓存实例
class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


class Spam3(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name


a = Spam3('Guido')
b = Spam3('Diana')
c = Spam3('Guido')
print(a is b)
print(a is c)


# 不使用元类的单例模式
class _Spam:
    def __init__(self):
        print('Creating Spam')


_spam_instance = None


def Spam4():
    global _spam_instance

    if _spam_instance is not None:
        return _spam_instance
    else:
        _spam_instance = _Spam()
        return _spam_instance


a = Spam4()
b = Spam4()