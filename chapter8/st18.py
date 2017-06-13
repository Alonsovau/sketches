# 利用Mixins扩展类功能
class LoggedMappingMixin:
    """
    Add logging to set/get/delete operations for debugging
    """
    __slots__ = () # 混入类都没有实例变量，因为直接实例化混入类没有任何意义

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)


class LoggedDict(LoggedMappingMixin, dict):
    pass


d = LoggedDict()
d['x'] = 23
d['x']
del d['x']


# 多线程的XML-RPC服务
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass



