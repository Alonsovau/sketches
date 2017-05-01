# 审查清理文本字符串
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = s.translate(remap)
print(s.translate(remap))

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
# 通过dict.fromkeys()方法构造一个字典，每个Unicode和音字符作为键，值都为None
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

digitmap = {
    c: ord('0') + unicodedata.digit(chr(c))
    for c in range(sys.maxunicode)
    if unicodedata.category(chr(c)) == 'Nd'
}
# 构造一个将所有Unicode数字字符映射到对应的ASCII字符上的表格
print(len(digitmap))
print(digitmap)
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))