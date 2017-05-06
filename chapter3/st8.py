# 分数运算
from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b, a * b)
c = a + b
print(c.numerator, c.denominator)
print(float(c))
print(c.limit_denominator(8))
x = 3.75
print(*x.as_integer_ratio())
print(x.as_integer_ratio())
print(Fraction(*x.as_integer_ratio()))