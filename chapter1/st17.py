# 合并多个字典或映射
from collections import ChainMap
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['y'])
print(c['z'])
# 先从a查找，查不到则去b查

print(len(c))
print(c.keys())
print(list(c.keys()))
print(list(c.values()))

c['z'] = 10
c['w'] = 11
del c['x']
print(a, b)
# del c['y']  出错，更新和删除操作总是影响列表中的第一个字典

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
values = values.parents
print(values, values['x'])
values = values.parents
print(values, values['x'])

a1 = {'x': 1, 'z': 3}
b1 = {'y': 2, 'z': 4}
merged = dict(b1)
merged.update(a1)
print(merged['x'], merged['y'], merged['z'])
a1['x'] = 13
print(merged['x'])
# 创建一个完全不同的字典对象或者破坏现有字典结构，原字典更新不会使得新的字典变化
# ChainMap使用原来的字典，不创建新字典
