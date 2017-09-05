# 捕获所有的异常
try:
    x = 1
except Exception as e:
    print(e)
# Exception捕获除了SystemExit,KeyboardInterrupt,GeneratorExit之外的所有异常
# 还想捕获这3个使用BaseException
