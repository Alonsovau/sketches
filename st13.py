# 过滤序列元素
from itertools import compress
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])

pos = (n for n in mylist if n>0)
print(pos)
mylist2 = []
for x in pos:
    mylist2.append(x)
print(mylist2)

values = ['1', '2', '-3', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int,values))
print(ivals)

print([n if n>0 else 0 for n in mylist])

addresses = [ '5412 N CLARK',
              '5148 N CLARK',
              '5800 E 58TH',
              '2122 N CLARK',
              '5645 N RAVENSWOOD',
              '1060 W ADDISON',
              '4801 N BROADWAY',
              '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n >5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))