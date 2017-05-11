# 同时迭代多个序列
from itertools import zip_longest
x = [1, 2, 3, 4, 5]
y = [9, 8, 7, 6, 5, 90]
for xv, yv in zip(x, y):
    print(xv, yv)
# 迭代长度跟参数中最短序列长度一致
for xv, yv in zip_longest(x, y, fillvalue=0):
    print(xv, yv)


headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
print(s)


a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)