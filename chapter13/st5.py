# 获取终端的大小
import os


sz = os.get_terminal_size()
print(sz)
print(sz.columns, sz.lines)
