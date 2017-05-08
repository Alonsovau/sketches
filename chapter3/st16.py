# 结合时区的日期操作
from datetime import datetime, timedelta
from pytz import timezone
import pytz

d = datetime(2017, 5, 28, 11, 11, 11)
print(d)
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later)  # 错误，应为3:15
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)
print('--------')
print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))
print(later_utc.astimezone(timezone(pytz.country_timezones['US'][0])))
print(str(pytz.country_timezones))
for key, value in pytz.country_timezones.items():
    print(key, value)
