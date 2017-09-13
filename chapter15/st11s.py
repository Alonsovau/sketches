import sample11
import array
import numpy
import timeit


a = array.array('d', [1, -3, 4, 7, 2, 0])
print(a)
sample11.clip(a, 1, 4, a)
print(a)

b = numpy.random.uniform(-10, 10, size=100000)
print(b)
c = numpy.zeros_like(b)
print(c)
sample11.clip(b, -5, 5, c)
print(min(c))
print(max(c))

print(timeit.timeit('numpy.clip(b, -5, 5, c)', 'from __main__ import b, c, numpy', number=1000))
print(timeit.timeit('sample11.clip(b, -5, 5, c)', 'from __main__ import b, c, sample11', number=1000))
# 书上运行结果是numpy快，因为numpy核心代码是c
# 而我这边是sample11快

# @cython.boundscheck(False
# @cython.wraparound(False)
# 省去数组越界检查、消除相对数组的负数下标处理，可以极大提升性能
