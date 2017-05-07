# 计算当前月份的日期范围
from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)# 取当月第一天
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    print(calendar.monthrange(start_date.year, start_date.month))
    # monthrange()返回该月第一天为周几和该月总共有多少天
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

a_day = timedelta(days=1)
first_day, last_day = get_month_range(date(year=2017, month=2, day=28))
while first_day < last_day:
    print(first_day)
    first_day += a_day

# 使用生成器创建一个类似内置函数range()的函数
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2017, 5, 28), datetime(2017, 5, 29),
                    timedelta(hours=6)):
    print(d)
