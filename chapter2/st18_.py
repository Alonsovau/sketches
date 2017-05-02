# 字符串令牌解析
text = 'foo = 23 + 42 * 10'
import re
NAME = r'(?P<NAME>[a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.scanner('foo = 42')
print(scanner.match())
match = scanner.match()
print(match.lastgroup, match.group())
print(scanner.match().lastgroup, match.group())
# 看不懂