# 序列上索引值迭代
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list, 1):
    print(index, value)


# 文件中出现的单词映射他出现的行号
from collections import defaultdict
word_summary = defaultdict(list)
with open('somefile.txt', 'r') as f:
    lines = f.readlines()
for inx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(inx)
for x, y in word_summary.items():
    print(x, y)


data = [(1,2), (3,4), (5,6)]
for x, (y, z) in enumerate(data):
    print(x, y, z)