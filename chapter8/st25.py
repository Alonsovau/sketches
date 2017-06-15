# 创建缓存实例
import logging, weakref


a = logging.getLogger('foo')
b = logging.getLogger('bar')
print(a is b)
c = logging.getLogger('foo')
print(a is c)

# 通常是编写一个工厂函数修改普通的实例创建，这里不使用


class Spam:
    _spam_cache = weakref.WeakValueDictionary()

    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print('Initializing Spam')
        self.name = name


s = Spam('Dave')
t = Spam('Dave')
print(s is t)
# 初看起来好像可以达到预期效果，但是问题是init()每次都会被调用，不管这个实例是否被缓存了


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

    def clear(self):
        self._cache.clear()


class Spam:
    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name
        print('Init')

    def get_spam(name):
        return Spam.manager.get_spam(name)


a = Spam.get_spam('foo')
b = Spam.get_spam('bar')
c = Spam.get_spam('foo')
print(a is c)
print(a is b)


class CacheSpamManager2:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            temp = Spam2._new(name)
            self._cache[name] = temp
        else:
            temp = self._cache[name]
        return temp

    def clear(self):
        self._cache.clear()


class Spam2:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")

    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self

csm = CacheSpamManager2()
a2 = csm.get_spam('foo')
b2 = csm.get_spam('bar')
c2 = csm.get_spam('foo')
print(a2 is c2)
print(a2 is b2)