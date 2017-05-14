print('ACM', 50, 91.5)
print('ACM', 50, 91.5, sep=',')
print('ACM', 50, 91.5, sep=',', end='!!\n')
for i in range(5):
    print(i, end=' ')
row = ('acme', 50, 91.5)
print()
print(*row, sep=',')