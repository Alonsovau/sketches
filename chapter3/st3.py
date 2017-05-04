# 数字的格式化输出
x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))
print(format(x, '0,.1f'))
print(format(x, 'e'))
print(format(x, '0.2E'))
print('The value is {:0,.2f}'.format(x))
from decimal import Decimal
d = Decimal('1234.56789')
print(format(d, '0.1f'))

swap_separators = {ord('.'): ',', ord(','): '.'}
print(format(x, ',').translate(swap_separators))
# 包含千位符的格式化跟本地化没有关系。如果你需要根据地区来显示千位符，
# 你需要自己去调查下locale模块中的函数了。
# 你同样也可以使用字符串的translate()方法来交换千位符。
