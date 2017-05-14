# 文件不存在才能写入
with open('somefile', 'wt') as f:
    f.write('Hello\n')
with open('somefile', 'xt') as f:
    f.write('Hello\n', 'wt')
# 要注意的是x模式是一个Python3对open()函数特有的扩展。
# 在Python的旧版本或者是Python实现的底层C函数库中都是没有这个模式的。
