# 字典中的键映射多个值
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d1 = defaultdict(set)
d1['a'].add(1)
d1['a'].add(2)
d1['b'].add(4)
print(d1)

d2 = {}
d2.setdefault('a', []).append(1)
d2.setdefault('a', []).append(2)
d2.setdefault('b', []).append(4)
print('d2:',d2)

pairs = {'a': 6, 'b': 4}
d3 = {'a':[1],'b':[0]}
for key, value in pairs:
    if key not in d3:
        d[key] = []
    d3[key].append(value)
print('d3:',d3)
for key, value in pairs.items():
    print('key[%s]=' % key, value)
