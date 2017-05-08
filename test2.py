# 计算程序运行时间
from datetime import datetime
import time, timeit
# begin = time.clock()
# begin = datetime.now()
begin = timeit.default_timer()
text = '2017-5-28'
y = datetime.strptime(text, '%Y-%m-%d')
# end = time.clock()
# end = datetime.now()
end = timeit.default_timer()
print(end - begin)

# time.clock()返回的是处理器时间，而因为Unix中jiffy的缘故,所以精度不会太高。clock转秒，除以1000000。
# 究竟是使用 time.clock()精度高，还是使用 time.time()精度更高，要视乎所在的平台来决定。
# 总概来讲，在Unix系统中，建议使用time.time()，在 Windows系统中，建议使用time.clock()。
# 我们要实现跨平台的精度性，我们可以使用timeit来代替time