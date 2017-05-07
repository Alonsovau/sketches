# 字符串转换为日期
from datetime import datetime
import os
text = '2017-5-28'
os.get
y = datetime.strptime(text, '%Y-%m-%d')
# strptime()性能差，使用纯python实现，必须处理所有的系统本地设置
z = datetime.now()
diff = z-y
print(diff)
nice_z = datetime.strftime(z, '%A %B %d, %Y') # 格式化日期
print(nice_z)

def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
