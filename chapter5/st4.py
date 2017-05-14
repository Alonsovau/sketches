# 读写字节数据
with open('somefile.class', 'rb') as f:
    data = f.read()
print(data)
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello world')
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    print(data)
    print(data.decode('utf-8'))

import array
nums = array.array('i', [1, 2, 4, 5])
with open('data.bin', 'wb') as f:
    f.write(nums)
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)
    print(a)
# 二进制I/O还有一个鲜为人知的特性就是数组和 C 结构体类型能直接被写入，而不需要中间转换为自己对象
# 它通常具有平台相关性，并且可能会 依赖字长和字节顺序 (高位优先和低位优先)
