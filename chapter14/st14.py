# 加速程序运行
# 在不使用c扩展、jit编译器情况下加速
import sys
import csv
import math


# 1
with open(sys.argv[1]) as f:
    for row in csv.reader(f):
        pass


# 2
def main(filename):
    with open(filename) as f:
        pass
main(sys.argv[1])
# 第一种使用全局变量，第二种放在函数中局部变量更快


# 1
def compute_roots(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result


# 2
from math import sqrt
def compute_roots2(nums):
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result


# test
nums = range(1000000)
for n in range(100):
    r = compute_roots(nums)
# 每一次使用(.)操作符访问属性都会带来额外开销，
# 触发特定的方法，比如__getattribute__()和__getattr__()，这些方法会进行字典操作
# 这些代码只有在例如循环的大量重复代码中才有意义


def compute_roots3(nums):
    sqrt = math.sqrt
    # 频繁访问sqrt，取出来放入一个局部变量中
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result



