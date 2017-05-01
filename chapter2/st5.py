# 字符串搜索和替换
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

from calendar import month_abbr


# 一个替换回调函数的参数是一个match对象，也就是match()或者find()返回的对象。
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))

newtext, n = datepat.subn(r'\3-\1-\2',text)
# 如果除了替换后的结果外，你还想知道有多少替换发生了，可以使用 re.subn()来代替。
print(newtext)
print(n)