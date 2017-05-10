# 迭代器切片
def count(n):
    while True:
        yield n
        n += 1


c = count(0)
import itertools
for x in itertools.islice(c, 10, 20):
    print(x)
# 迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道
# (并且也没有实现索引)。函数islice()返回一个可以生成指定元素的迭代器，
# 它通过遍历并丢弃直到切片开始索引位置的所有元素。然后才开始一个个的返回元素，
# 并直到切片结束索引位置。