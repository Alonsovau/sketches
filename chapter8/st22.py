# 不用递归实现访问者模式
import types


class Node:
    pass


class NodeVisitor:
    def visit(self, node):
        stack = [node]
        last_result = Node
        while stack:
            try:
                last = stack
