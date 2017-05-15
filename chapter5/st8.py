# 固定大小记录的文件迭代
from functools import partial
RECORD_SIZE = 32
with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read(), RECORD_SIZE), b'')
    for r in records:
        pass
# functools.partial用来创建一个每次被调用时从文件中读取固定数目字节的可调用对象
# iter迭代器一直调用可调用对象直到他返回标记值，上述b''就是达到文件尾的返回值
