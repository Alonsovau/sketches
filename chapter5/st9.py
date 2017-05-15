# 读取二进制数据到可变缓冲区中
import os.path
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf
with open('somefile.bin', 'wb') as f:
    f.write(b'hello world')
buf = read_into_buffer('somefile.bin')
print(buf)
buf[0:5] = b'hallo'
print(buf)
# 和普通read()方法不同的是，readinto()填充已存在的缓冲区而不是为新对象重新分配内存再返回它
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)
m2[:] = b'WORLD'
print(buf)
# memoryview可以通过零复制的方式对已存在的缓冲区执行切片操作，甚至还能修改它的内容