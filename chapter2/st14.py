# 合并拼接字符串
parts = ['Is', 'Chicago', 'Not', 'Chicago']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

a = 'Hello' 'World'
# 无需+号
print(a)

# s = ''
# for p in parts:
#     s += p
# +号连接字符串非常低效率，+号连接会引起内存复制以及垃圾回收，每一次+=会创建一个新的字符串对象

data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))
