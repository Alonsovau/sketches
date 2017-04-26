# 通过某个关键字排序一个字典列表
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid':1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)

# 等价于
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
print(rows_by_fname)
rows_by_lfname = sorted(rows, key=lambda r:(r['lname'],r['fname']))
print(rows_by_lfname)
# itemgetter速度较快

print(min(rows, key=itemgetter('uid')))