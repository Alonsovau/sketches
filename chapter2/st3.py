# 用shell通配符匹配字符串
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

print(fnmatch('l.txt', '*.TXT'))
# mac下为false
print(fnmatchcase('l.txt','*.TXT'))
addresses = ['5412 N CLARK ST',
             '1060 W ADDISON ST',
             '1039 W GRANVILLE AVE',
             '2122 N CLARK ST',
             '4802 N BROADWAY']
print([addr for addr in addresses if fnmatch(addr, '*ST')])