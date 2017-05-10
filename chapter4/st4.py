# 实现迭代器协议,构建一个能支持迭代操作的自定义对象,并希望找到一个能实现迭代的简单方法
from collections import Iterable,Iterator


class Node:
    def __init__(self, value):
        self._value = value
        self._child = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._child.append(node)

    def __iter__(self):
        return iter(self._child)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


# 关联迭代器实现
class Node2:
    def __init__(self, value):
        self._value = value
        self._child = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._child.append(node)

    def __iter__(self):
        return iter(self._child)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        else:
            self._child_iter = next(self._child_iter).depth_first()
            return next(self)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)

    # root = Node2(0)
    # child1 = Node2(1)
    # child2 = Node2(2)
    # root.add_child(child1)
    # root.add_child(child2)
    # child1.add_child(Node2(3))
    # child1.add_child(Node2(4))
    # child2.add_child(Node2(5))
    # print(root.depth_first().__next__().depth_first().__next__())
