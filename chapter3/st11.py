# 随机选择
import random
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.sample(values, 2))
print(random.sample(values, 3))
# 提取出N个不同元素样本
random.shuffle(values)
print(values)
# 打乱序列顺序
print(random.randint(0,10))
# 生成随机整数
print(random.random(), random.random())
# 生成0-1范围内均匀分布的浮点数
print(random.getrandbits(200))
# 生成N位随机位(二进制)整数


# random 模块使用 Mersenne Twister算法来计算生成随机数。这是一个确定性算法，
# 但是你可以通过random.seed()函数修改初始化种子。
# 比如：
random.seed() # Seed based on system time or os.urandom()
random.seed(12345) # Seed based on integer given
random.seed(b'bytedata') # Seed based on byte data