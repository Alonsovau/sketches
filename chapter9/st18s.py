import operator, types, sys


def name_tuple(classname, fieldnames):
    cls_dict = {
        name : property(operator.itemgetter(n)) for n, name in enumerate(fieldnames)
    }

    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    # make the class
    cls = types.new_class(classname, (tuple,), {}, lambda ns: ns.update(cls_dict))
    # set the module to that of the caller
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls


Point = name_tuple('Point', ['x', 'y'])
print(Point)
p = Point(4, 5)
print(len(p))
print(p.x, p.y)
print('%s %s' %p)
# 这种方法的问题在于它忽略了一些关键步骤，比如对于元类中__prepare__()方法的调用，
# 通过types.new_class()，可以保证所有的必要初始化步骤都能得到执行，比如types.new_class()第四个参数的
# 回调函数接受__prepare__()方法返回的映射对象
# p.x = 2

# 如果只想执行准备步骤，可以使用types.prepare_class()
metaclass, kwargs, ns = types.prepare_class('Stock', (), {'metaclass': type})
print(metaclass, kwargs, ns)
# 可参考PEP3115
