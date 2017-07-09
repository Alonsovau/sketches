# 使用相对路径名导入包中子模块
# mypackage/
#     __init__.py
#     A/
#         __init__.py
# spam.py
# grok.py B/
#         __init__.py
#         bar.py
# 如果模块 mypackage.A.spam 要导入同目录下的模块 grok，它应该包括的 import 语句如下:
# from . import grok
# from ..B import bar