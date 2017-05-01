# 最短匹配模式
import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
# 本来的意图是匹配被双引号包含的文本，*操作符是贪婪的，会查找最长的可能匹配
str_pat2 = re.compile(r'\"(.*?)\"')
print(str_pat2.findall(text2))
