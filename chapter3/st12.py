# 基本的日期与时间转换
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days, c.seconds, c.seconds / 3600, c.total_seconds() / 3600)
from datetime import datetime
a = datetime(2017, 5, 28)
print(a + timedelta(days=2))
b = datetime(2017, 5, 1)
d = b - a
print(d.days)
now = datetime.today()
print(now)

from dateutil.relativedelta import relativedelta
print(a + relativedelta(months=+8))

