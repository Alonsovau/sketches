# 拆解Python字节码
import dis, opcode


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('Blastoff')


dis.dis(countdown)
print(countdown.__code__.co_code)
c = countdown.__code__.co_code
c0 = opcode.opname[c[0]]
print(c0)

# 处理字节码，见cookbook