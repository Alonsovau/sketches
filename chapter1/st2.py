# 查找最大或者最小的N个元素
import heapq

nums=[1,2,3,9,8,7,-5,2,33]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

portfolio=[
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'AAPL','shares':50,'price':543.22},
    {'name':'FB','shares':200,'price':21.09},
    {'name':'HPQ','shares':35,'price':31.75}
]
cheap=heapq.nsmallest(3,portfolio,key=lambda s:s['price'])
expensive=heapq.nlargest(3,portfolio,key=lambda s:s['price'])
print(cheap)
print(expensive)

numss=[8,6,90,-9,0,6,-55]
heapq.heapify(numss)
print(numss)
heapq.heappop(numss)
print(numss)
#求单个元素
print(max(numss))
print(min(numss))
#
print(sorted(numss)[:5])
print(numss)
print(sorted(numss)[-4:])