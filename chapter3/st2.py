# 执行精确的浮点数运算
a = 4.2
b = 2.1
print(a + b)
print((a + b) == 6.3)
# 这些错误是由底层CPU和IEEE754标准通过自己的浮点单位去执行算术时的特征。
# 由于Python的浮点数据类型使用底层表示存储数据，因此你没办法去避免这样的误差。
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
print(a + b == Decimal('6.3'))

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)
# decimal模块的一个主要特征是允许你控制计算的每一方面，包括数字位数和四舍五入运算。
# 为了这样做，你先得创建一个本地上下文并更改它的设置

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))

import math
print(math.fsum(nums))