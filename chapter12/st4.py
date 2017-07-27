import threading


class SharedCounter:
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        with self._value_lock:
            self._value += delta

    def decr(self, delta=1):
        with self._value_lock:
            self._value -= delta
# Lock对象和with语句块一起使用可以保证互斥执行
# 就是每次只有一个线程可以执行with语句包含的代码块
# with语句会在这个代码块执行前自动获取锁，在执行结束后自动释放锁


class SharedCounter2:
    _lock = threading.RLock()

    def __init__(self, initial_value = 0):
        self._value = initial_value

    def incr(self, delta=1):
        with SharedCounter2._lock:
            self._value += delta

    def decr(self, delta=1):
        with SharedCounter2._lock:
            self._value -= delta
# 一个RLock（可重入锁）可以被同一个线程多次获取
# 主要用来实现基于监测对象模式的锁定和同步
# 在使用这种锁的情况下，当锁被持有时，只有一个线程可以使用完整的函数或者类中的方法
