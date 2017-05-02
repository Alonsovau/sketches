# 字节字符串上的字符串操作
data = b'hello world'
print(data[0:5])
print(data.startswith(b'hello'))
print(data.split())
print(data.replace(b'hello', b'hello zx'))

data = bytearray(b'hello world')
print(data[0:5])
print(data.startswith(b'hello'))
print(data.split())
print(data.replace(b'hello', b'hello zx'))

data = b'FOO:BAR,SPAM'
import re
# re.split('[:,]', data)
print(re.split(b'[:,]', data))

a = 'hello world'
print(a[0])
b = b'hello world'
print(b[0])

