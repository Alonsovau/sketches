# 在序列上保持元素顺序并消除重复的值
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 2, 3, 4, 9, 8, 7, 6, 9, 10, 4, 6]
print(list(dedupe(a)))


# 想要消除的元素不是hashable
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe2(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe2(a, key=lambda d: d['x'])))
