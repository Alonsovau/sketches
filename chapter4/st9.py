# 排列组合的迭代
from itertools import permutations, combinations, combinations_with_replacement
items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)
for p in permutations(items, 2):
    print(p)
for c in combinations(items, 2):
    print('c:', c)
for c in combinations_with_replacement(items, 2):
    print('cwr:', c)