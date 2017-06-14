# 循环引用数据结构的内存管理
import weakref, gc


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


root = Node('parent')
c1 = Node('child')
root.add_child(c1)
print(c1.parent)
del root
print(c1.parent)


class Data:
    def __del__(self):
        print('Data.__del__')


class Node1:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Data()
del a
a = Node1()
del a
aa = Node1()
aa.add_child(Node1())
del aa
gc.collect()
# 需在3.3环境中运行，3.5与书中预期结果不一样
