# 创建大量对象时节省内存方法(可能上百万)
import sys


class Date:
    __solts__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class Date2:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

date = Date(2012, 12, 12)
print(sys.getsizeof(date))
date2 = Date2(2012, 12, 12)
print(sys.getsizeof(date2))