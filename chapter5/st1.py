import sys
with open('somefile.txt', 'rt') as f:
    data = f.read()
print(data)
with open('somefile.txt', 'wt') as f:
    f.write('s')
print(sys.getdefaultencoding())
with open('somefile.txt', 'at', encoding='latin-1') as f:
    f.write('lala')
# 当读取一个未知编码的文本时使用latin-1编码永远不会产生解码错误。
# 使用latin-1编码读取一个文件的时候也许不能产生完全正确的文本解码数据，但是它也能从中提取出足够多的有用数据。
# 同时，如果你之后将数据回写回去，原先的数据还是会保留的。
