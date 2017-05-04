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

s = b'Hello World'
print(s.decode('ascii'))

print('{:10s}{:10d}{:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))
# 格式化字节字符串，先使用标准字符串，然后将其编码为字节字符串

with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')
import os
print('jalape\xf1o.txt'.encode('utf8'))
print(os.listdir('.'))
print(os.listdir(b'.'))
