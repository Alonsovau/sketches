# 将模块分割成多个文件
# 你想将一个模块分割成多个文件。但是你不想将分离的文件统一成一个逻辑模块时 使已有的代码遭到破坏。
# mymodule/
# __init__.py
# a.py
# b.py
# a.py class A: def spam(self): print('A.spam')
# b.py from .a import A class B(A): def bar(self): print('B.bar')
# __init__.py from .a import A from .b import B
# >>> import mymodule >>> a = mymodule.A() >>> a.spam() A.spam >>> b = mymodule.B() >>> b.bar() B.bar


# 延迟导入: init .py 文件一次导入所有必需的组件的。但是对于一个很大的模块，可能你只想组件在需要时被加载。要做到 这一点， init .py 有细微的变化
# __init__.py def A(): from .a import A return A() def B(): from .b import B return B()
# 延迟加载的主要缺点是继承和类型检查可能会中断。你可能会稍微改变你的代码
# if isinstance(x, mymodule.A): # Error
# if isinstance(x, mymodule.a.A): # Ok
