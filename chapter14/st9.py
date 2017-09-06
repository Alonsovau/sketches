# 捕获异常后抛出另外的异常
def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e


try:
    example()
except RuntimeError as e:
    print("It didn't work:", e)
    if e.__cause__:
        print('Cause:', e.__cause__)


def example2():
    try:
        int('N/A')
    except ValueError as e:
        print("Couldn't parse:", err)


# example2()
# 获得2个异常信息，NameError作为程序的最终异常被抛出，而不是位于解析异常的直接回应中


def example3():
    try:
        int('N/A')
    except ValueError:
        raise RuntimeError('A parsing error occurred ') from None
example3()
# 使用raise from None忽略异常链


class SomeException(Exception):
    pass


class DifferentException(SomeException):
    pass


try:
    i = 1
except SomeException as e:
    raise DifferentException() from e
# 大多数情况都应该使用raise from
