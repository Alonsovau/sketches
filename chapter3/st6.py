# 复数的数学运算
a = complex(2, 4)
b = 3 - 5j
print(a, b)
print(a.real, a.imag, a.conjugate())
print(a + b, a * b, a /b, abs(a))
import cmath
print(cmath.sin(a))

import numpy as np
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a + 2)
print(np.sin(a))

print(cmath.sqrt(-1))