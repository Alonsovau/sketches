# 编码解码base64数据
import base64
s = b'hello'
a = base64.b64encode(s)
print(a)
print(base64.b64decode(a))
a = base64.b64encode(s).decode('ascii')
print(a)