# 字符串的I/O操作
import io
s = io.StringIO()
s.write('Hello world\n')
print('this is a test', file=s)
print(s.getvalue())

s = io.StringIO('Hello\nworld\n')
print(s.read(4))
print(s.read())

s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
# 当你想模拟一个普通的文件的时候 StringIO 和 BytesIO 类是很有用的。
# 比如，在 单元测试中，你可以使用 StringIO 来创建一个包含测试数据的类文件对象，这个对象 可以被传给某个参数为普通文件对象的函数。
# 需要注意的是， StringIO 和 BytesIO 实例并没有正确的整数类型的文件描述符。
# 因此，它们不能在那些需要使用真实的系统级文件如文件，管道或者是套接字的程序 中使用。
