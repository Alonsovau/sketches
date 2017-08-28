# 终止程序并给出错误信息
raise SystemExit('It failed!')
# 等价于下面代码
# import sys
# sys.stderr.write('It failed!\n')
# raise SystemExit(1)
