from xmlrpc.client import ServerProxy


s = ServerProxy('http://localhost:15000', allow_none=True)
s.set('foo', 'bar')
s.set('spam', [1, 2, 3])
print(s.keys())
print(s.get('foo'))
print(s.get('spam'))
s.delete('spam')
print(s.exists('spam'))


print('除字符串、整形、列表、字典外数据类型：')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
s.set('foo', p)
print(s.get('foo'))
s.set('foo1', b'hello world')
v = s.get('foo1')
print(v)
print(type(v))
