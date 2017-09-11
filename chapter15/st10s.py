import sample
import array

print(sample.gcd(42, 10))
print(sample.in_mandel(0, 0, 400))
print(sample.divide(42, 10))
a = array.array('d', [1, 2, 3])
print(sample.avg(a))
p1 = sample.Point(2, 3)
p2 = sample.Point(4, 5)
print(p1, p2)
print(sample.distance(p1, p2))
