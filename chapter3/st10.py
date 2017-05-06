# 矩阵与线性代数运算
import numpy as np
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
print(m.T)
# 转置矩阵(transpose)
print(m.I)
# 逆矩阵(inverse)
v = np.matrix([[2], [3], [4]])
print(v)
print(m * v)

import numpy.linalg
print(numpy.linalg.det(m))
print(1*(-36-40)--2*(0-35)+3*(0-28))
# 行列式计算(determinant)

print(numpy.linalg.eigvals(m))
# 求特征值(eigenvalue)

x= numpy.linalg.solve(m, v)
print(x)
# 求解 mx = v
print(m * x)
