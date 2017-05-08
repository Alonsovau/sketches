# 使用生成器创建新的迭代模式
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment
# 生产某个范围内浮点数的生成器
for n in frange(0, 4, 0.5):
    print(n)