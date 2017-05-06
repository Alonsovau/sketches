# 无穷大和NaN
import math
a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)
print(math.isinf(a), math.isnan(c))
print(a + 45, a * 10, 10 / a)
print(a + b)