# 字符串转换为日期
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

from datetime import datetime
import timeit,time
text = '2017-5-28'
start1 = time.clock()
y = datetime.strptime(text, '%Y-%m-%d')
end1 = time.clock()
# strptime()性能差，使用纯python实现，必须处理所有的系统本地设置
start2 = time.clock()
yy = parse_ymd(text)
end2 = time.clock()
print(end1 - start1, end2 - start2)
z = datetime.now()
diff = z-y
print(diff)
nice_z = datetime.strftime(z, '%A %B %d, %Y') # 格式化日期
print(nice_z)


