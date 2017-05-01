# 字符串开头或结尾匹配
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))

import os
filenames = os.listdir('./chapter2')
print(filenames)
print([name for name in filenames if name.endswith('2.py')])

from urllib.request import urlopen


def read_data(name):
    if name.startswith('http:', 'https:', 'ftp:'):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:', 'ftp:']
url = 'http://www.baidu.com'
# url.endswith(choices)
# 参数必须为元组
print(url.startswith(tuple(choices)))