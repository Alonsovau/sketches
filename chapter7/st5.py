# 定义有默认参数的函数
def spam(a, b=42):
    print(a, b)
spam(1)
spam(1, 9)

_no_value = object()


def spam(a, b=_no_value):
    if b is _no_value: print('No b value supplied')
    print(b)
spam(1)
spam(1, 2)
spam(1, None)


x = 77
def spamm(a, b=x):
    print(a, b)
spamm(1)
x = 78
spamm(1)


def spam1(a, b=[]):
    print(b)
    return b

x = spam1(1)
print(x)
x.append(99)
print(x)
spam1(1)