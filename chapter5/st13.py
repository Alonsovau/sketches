# 获取文件夹中的文件列表
import os

names = [name for name in os.listdir('c:/')
         if os.path.isfile(os.path.join('c:/', name))]
print(names)
# get all regular files
dirnames = [name for name in os.listdir('c:/')
            if os.path.isdir(os.path.join('c:/', name))]
print(dirnames)
# get all dirs
exefiles = [name for name in os.listdir('c:/')
           if name.endswith('.exe')]
print(exefiles)
import glob
exefiles1 = glob.glob('c:/*.exe')
print(exefiles1)
from fnmatch import fnmatch
exefiles2 = [name for name in os.listdir('c:/')
             if fnmatch(name, '*.exe')]
print(exefiles2)

file_metadata = [(name, os.stat(name)) for name in exefiles1]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)