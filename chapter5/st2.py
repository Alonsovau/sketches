# 打印输出至文件中
with open('somefile1.txt', 'wt') as f:
    print('Hello World!', file=f)
# 有一点要注意的就是文件必须是以文本模式打开。
# 如果文件是二进制模式的话，打印就会出错