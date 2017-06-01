# 给函数参数增加元信息
def add(x:int, y:int) -> int:
    return x + y
print(help(add))
print(add.__annotations__)