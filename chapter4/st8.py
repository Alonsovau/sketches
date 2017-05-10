# 跳过可迭代对象的开始部分
with open('somefile.txt') as f:
    for line in f:
        print(line, end='')
print()


from itertools import dropwhile
with open('somefile.txt') as f:
    for line in dropwhile(lambda l: l.startswith('#'), f):
        print(line, end='')
print()

from itertools import islice
items = ['a', 'b', 'c', 1, 2, 4]
for x in islice(items, 3, None):
    print(x)