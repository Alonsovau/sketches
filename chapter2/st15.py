# 字符串中插入变量
s = '{name} has {n} messages.'
print(s.format(name='Guido', n=21))

name = 'Guido'
n = 37
print(s.format_map(vars()))
# 替换的变量在变量域中能找到，可以使用上述方法

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('z', '12')
print(s.format_map(vars(a)))
# vars()适用于对象实例

# print(s.format(name='Guido'))
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

print(s.format_map(safesub(vars())))
# 假设没有n变量
# 理想输出：'Guido has {n} messages.'

import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
print(sub('Hello {name}, my favorite color is {color}'))
