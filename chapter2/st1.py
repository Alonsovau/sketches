# 使用多个界定符分割字符串
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[;,\s]\s*', line))
fields = re.split(r'(;|,|\s)\s*', line)
# 括号捕获分组，被匹配的文本也将出现在结果列表中
print(fields)
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
print(''.join(v+d for v,d in zip(values, delimiters)))
print(re.split(r'(?:,|;|\s)\s*', line))
# 你不想保留分割字符串到结果列表中去，但仍然需要使用到括号来分组正则表达式的话，
# 确保你的分组是非捕获分组，形如 (?:...)
