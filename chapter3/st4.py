x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x, 'b'), format(x, 'o'), format(x, 'x'))
# 不输出0b,0o,0x前缀

x = -1234
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x, 'b'), format(x, 'o'), format(x, 'x'))

print(format(2**32 + x, 'b'))
print(format(2**32 + x, 'x'))
# 如果你想产生一个无符号值，你需要增加一个指示最大位长度的值。
# 比如为了显示32位的值，

print(int('4d2', 16))
print(int('10011010010', 2))