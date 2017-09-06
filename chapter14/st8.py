# 创建自定义异常
class NetworkError(Exception):
    pass


class HostnameError(NetworkError):
    pass


class TimeoutError(NetworkError):
    pass


class ProtocolError(NetworkError):
    pass


try:
    a = 1
except TimeoutError as e:
    print(e)
except ProtocolError as e:
    print(e)

print(FileExistsError.__mro__)
# 自定义异常类应集成Exception类或其子类
# 虽然所有的类都继承自BaseException，但是不应该使用
# 继承BaseException可能导致自定义异常不会被捕捉而发送信号退出程序运行


class CustomError(Exception):
    def __init__(self, message, status):
        super().__init__(self, message, status)
        self.message = message
        self.status = status


try:
    raise RuntimeError('it failed')
except RuntimeError as e:
    print(e.args)
try:
    raise RuntimeError('It failed', 42, 'spam')
except RuntimeError as e:
    print(e.args)
# 接收所有传递的参数并以元组的形式存储在args属性中
