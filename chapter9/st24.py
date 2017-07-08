# 解析与分析Python源码
import ast


x = 42
print(eval('2 + 3*4 + x'))
exec('for i in range(10): print(i)')


ex = ast.parse('2 + 3*4 + x', mode='eval')
print(ex)
print(ast.dump(ex))
top = ast.parse('for i in range(10): print(i)', mode='exec')
print(top)
print(ast.dump(top))


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
    top = ast.parse(code, mode='exec')
    c = CodeAnalyzer()
    c.visit(top)
    print('Loaded:', c.loaded)
    print('Stored:', c.stored)
    print('Deleted:', c.deleted)
    exec(compile(top, '<stdin>', 'exec'))