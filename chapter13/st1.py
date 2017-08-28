#!/usr/bin/env python3
# 通过重定向／管道／文件接收输入
import fileinput


with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')
with fileinput.input('/etc/passwd') as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')