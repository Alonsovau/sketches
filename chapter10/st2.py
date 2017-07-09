# 控制模块被全部导入的内容
# 当使用’from module import *‘ 语句时，希望对从模块或包导出的符号进行精确控 制
def spam():
    pass


def grok():
    pass


blah = 42
__all__ = ['spam', 'grok']
# 在你的模块中定义一个变量 all 来明确地列出需要导出的内容