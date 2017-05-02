import re
str = input('请输入：')
char_pat = re.compile(r'[a-zA-Z]')
int_pat = re.compile(r'\d')
char_num = len(char_pat.findall(str))
int_num = len(int_pat.findall(str))
print('字符数：{}'.format(char_num))
print('数字数：{}'.format(int_num))
print('其他字符数：{}'.format(len(str) - int_num - char_num))

int_num2 = 0
char_num2 = 0
other_num = 0
for ch in str:
    if ch.isdigit():
        int_num2 += 1
    elif ch.isalpha():
        char_num2 += 1
    else:
        other_num += 1
print('字符数：{}'.format(char_num2))
print('数字数：{}'.format(int_num2))
print('其他字符数：{}'.format(other_num))
# 中文使用isalpha判断 会有出入 str.encode('utf8')???
print('周'.isalpha())
print(re.findall( '[\u4e00-\u9fa5]', '周周4iyi以'))
# 匹配中文字符