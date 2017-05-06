# 字节到大整数的打包与解包
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

import struct
h1, lo = struct.unpack('>QQ', data)
print((h1 << 64) + lo)

x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))

import re
x = 523 ** 23
print(re.findall(r'\d', str(x)))
print(x.bit_length())
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
print(x.to_bytes(nbytes, 'little'))
