# 定义匿名或内联函数
add = lambda x, y: x + y
print(add(2, 3))
print(add('hello', 'world'))

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key = lambda name:name.split()[-1].lower()))
