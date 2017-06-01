# 只接受关键字参数的函数
def recv(maxsize, *, block):
    pass
# recv(1024, True) # 错
recv(1024, block=True)

def minium(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m
print(minium(1, 5, 2, -5, 10))
print(minium(1, 5, 2, -5, 10, clip=0))