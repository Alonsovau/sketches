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
