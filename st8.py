# 命名切片
a = slice(1, 7, 2)
print(a.start, a.stop, a.step)
items = [1, 2, 3, 4, 5, 6, 7]
print(items[a])

# indices返回三元组 使得值符合边界限制 避免IndexError
s = 'helloworld'
b = slice(1, 1000, 2)
print(b.indices(len(s)))
for i in range(*b.indices(len(s))):
    print(s[i])
