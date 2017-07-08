# 在局部变量域中执行代码
# a = 13
# exec('b = a + 1')
# print(b)


def test():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)


test()


def test2():
    x = 0
    loc = locals()
    print('before:', loc)
    exec('x += 1')
    print('after:', loc)
    print('x = ', x)


test2()


def test3():
    x = 0
    loc = locals()
    print('test3', loc)
    exec('x += 1')
    print('test3', loc)
    locals()
    print('test3', loc)


test3()


def test4():
    a = 13
    loc = {'a': a}
    glb = {}
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print('test4', b)


test4()