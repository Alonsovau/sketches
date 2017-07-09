# 解析与分析Python源码
import ast, inspect


x = 42
print(eval('2 + 3*4 + x'))
exec('for i in range(10): print(i)')


ex = ast.parse('2 + 3*4 + x', mode='eval')
print(ex)
print(ast.dump(ex))
top1 = ast.parse('for i in range(10): print(i)', mode='exec')
print(top1)
print(ast.dump(top1))


# 源码树是由一系列AST节点组成的，分析这些节点最简单的方法就是定义一个访问者类
# 实现很多visit_NodeName()方法
class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)


if __name__ == '__main__':
    code = '''for i in range(10):
                print(i)
                del i
    '''
    top1 = ast.parse(code, mode='exec')
    c = CodeAnalyzer()
    c.visit(top1)
    print('Loaded:', c.loaded)
    print('Stored:', c.stored)
    print('Deleted:', c.deleted)
    exec(compile(top1, '<stdin>', 'exec'))


# 下面是一个装饰器，通过重新解析函数体源码，重写AST并重新创建函数代码对象来将全局访问变量降为函数体作用范围
class NameLower(ast.NodeVisitor):
    def __init__(self, lowered_names):
        self.lowered_names = lowered_names

    def visit_FunctionDef(self, node):
        code = '__globals = globals()\n'
        code += '\n'.join("{0} = __globals['{0}']".format(name)
                          for name in self.lowered_names)
        code_ast = ast.parse(code, mode='exec')
        node.body[:0] = code_ast.body
        self.func = node


def lower_names(*namelist):
    def lower(func):
        srclines = inspect.getsource(func).splitlines()
        for n, line in enumerate(srclines):
            if '@lower_names' in line:
                break
        src = '\n'.join(srclines[n+1:])
        if src.startswith((' ','\t')):
            src = 'if 1:\n' + src
        top = ast.parse(src, mode='exec')
        cl = NameLower(namelist)
        cl.visit(top)
        temp = {}
        exec(compile(top, '', 'exec'), temp, temp)
        func.__code__ = temp[func.__name__].__code__
        return func
    return lower


INCR = 1


@lower_names('INCR')
def countdown(n):
    while n > 0:
        n -= INCR
