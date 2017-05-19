# 忽略文件名编码
import sys, os, fnmatch
print(sys.getfilesystemencoding())
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')
names = [name for name in os.listdir('.')
         if name.endswith('.txt')]
print(names)
names = [name for name in os.listdir('.')
          if fnmatch.fnmatch(name, '*.txt')]
print(names)
print(os.listdir(b'.'))