# 读写二进制数组数据
from struct import Struct
def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


if __name__=='__main__':
    records = [
        (1, 2.3, 4.5),
        (6, 7.8, 9.0),
        (12, 13.4, 56.7)
    ]
    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)


def read_records(format, f):
    record_strut = Struct(format)
    chunks = iter(lambda : f.read(record_strut.size), b'')
    return (record_strut.unpack(chunk) for chunk in chunks)
# 以块的形式增量读取文件


if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            print(rec)


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))
# 一次性读取到一个字节字符串中，然后分片解析

if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        data = f.read()
    for rec in unpack_records('<idd', data):
        print(rec)


record_struct = Struct('<idd')
print(record_struct.size)
print(record_struct.pack(1, 2.0, 3.0))
print(record_struct.unpack(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'))

import struct
print(struct.pack('<idd', 1, 2.0, 3.0))
print(struct.unpack('<idd', b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'))


f = open('data.b', 'rb')
chunks = iter(lambda :f.read(20), b'')
print(chunks)
for chk in chunks:
    print(chk)


def read_records(format, f):
    record_struct = Struct(format)
    while True:
        chk = f.read(record_struct.size)
        if chk == b'':
            break
        yield record_struct.unpack(chk)


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack(data[offset:offset + record_struct.size]
                                 for offset in range(0, len(data), record_struct.size)))
# 此方法不好，应使用上面的unpack_from()


from collections import namedtuple
Record = namedtuple('record', ['kind', 'x', 'y'])
with open('data.b', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))
    for r in records:
        print(r.kind, r.x, r.y)


import numpy as np
f = open('data.b', 'rb')
records = np.fromfile(f, dtype='<i,<d,<d')
print(records)
