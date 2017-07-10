# 通过字符串名导入模块
import importlib
math = importlib.import_module('math')
print(math.sin(2))
mod = importlib.import_module('urllib.request')
u = mod.urlopen('http://www.qq.com')


# import module() 也可用于相对导入
b = importlib.import_module('.b', __package__)