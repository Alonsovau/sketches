# 读取压缩文件
import gzip, bz2
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)
# 默认压缩等级是9，等级越低性能越好
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
