prices={
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price,max_price)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

prices_and_names = zip(prices.values(), prices.keys())
# zip函数创建的是一个只能访问一次的迭代器
print(min(prices_and_names))
# print(max(prices_and_names))

print(min(prices))
print(max(prices))
# 仅仅作用于键

print(min(prices.values()))
print(min(prices,key=lambda k:prices[k]))
min_value=prices[min(prices,key=lambda k:prices[k])]
print(min_value)
# 麻烦

same_prices = {'AAA': 12, 'AAZ': 12}
print(min(zip(same_prices.values(), same_prices.keys())))
print(max(zip(same_prices.values(), same_prices.keys())))
# 值相同时，返回最小或最大键值的实体会返回

a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}
print(a.keys() - b.keys())
print(a.items() & b.items())
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
