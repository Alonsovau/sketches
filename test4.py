# 利用yield from从生成器读取数据
def reader():
    for i in range(4):
        yield '<<{}'.format(i)


def reader_wrapper(g):
    yield from g


wrapper = reader_wrapper(reader())
for i in wrapper:
    print(i)


#利用yield from语句向生成器传送数据
def writer():
    while True:
        w = yield
        print('>>', w)


def writer_wrapper(coro):
    yield from coro  #等价于下面两种
# def writer_wrapper(coro):
#     coro.send(None)  #生成器准备接收数据
#     while True:
#         try:
#             x = yield
#             coro.send(x)
#         except StopIteration:
#             pass
# def writer_wrapper(coro):
#     coro.send(None)
#     while True:
#         try:
#             try:
#                 x = yield
#             except Exception as e:
#                 coro.throw(e)
#             else:
#                 coro.send(x)
#         except StopIteration:
#             pass

w = writer()
wrap = writer_wrapper(w)
wrap.send(None)
for i in range(4):
    wrap.send(i)


# 利用yield from向生成器传送数据--处理异常
class SpamException(Exception):
    pass


def writer():
    while True:
        try:
            w = yield
        except SpamException:
            print('***')
        else:
            print('3>>', w)


w = writer()
wrap = writer_wrapper(w)
wrap.send(None)
for i in [0, 1, 2, 'spam', 4]:
    if i == 'spam':
        wrap.throw(SpamException)
    else:
        wrap.send(i)