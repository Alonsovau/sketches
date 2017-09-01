# 通过文件名查找文件
import os
import sys
import time


def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(start, relpath, name, dirs, files)
            print(full_path)
            print(os.path.normpath(os.path.abspath(full_path)))
# os.path.abspath()接收路径，返回绝对路径
# os.path.normpath()返回正常路径，可以解决双斜杠、对目录多重引用等问题


def modified_within(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath):
                mtime = os.path.getmtime(fullpath)
                if mtime > (now - seconds):
                    print(fullpath)
# 列出在seconds内修改过的文件


if __name__ == '__main__':
    # findfile(sys.argv[1], sys.argv[2])
    if len(sys.argv) != 3:
        print('UsageL {} dir seconds '.format(sys.argv[0]))
        raise SystemExit
    modified_within(sys.argv[1], float(sys.argv[2]))
