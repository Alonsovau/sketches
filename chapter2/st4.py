# 字符串匹配和搜索
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
if re.match(r'\d+/\d+\d+', text1):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d')
if datepat.match(text1):
    print('yes')
else:
    print('no')
if datepat.match(text2):
    print('yes')
else:
    print('no')
# 如果你想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象。

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat2.match('11/12/2017')
print(m)
print(m.group(0)+','+m.group(1)+','+m.group(2)+','+m.group(3))
print(m.groups())
print(datepat2.findall(text))
for day, month, year in datepat2.findall(text):
    print('{}-{}-{}'.format(year, month, day))
for m in datepat2.finditer(text):
    print(m.groups())
