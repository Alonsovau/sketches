# 映射名称到序列元素
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub=Subscriber('alonsovau@outlook.com', '2017-4-26')
print(sub)
print(sub.addr, sub.joined)
print(len(sub))
addr, joined = sub
print(joined,addr)


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost2(records):
    total = 0.0
    for rec in records.items():
        s = Stock(*rec)
    total += s.shares * s.price
    return total
# records={'ACME':100, 123}
# print(compute_cost(records))
# print(compute_cost2(records))
