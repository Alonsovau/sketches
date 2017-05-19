# 创建临时文件和文件夹
from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory


with TemporaryFile('w+t') as f:
    f.write('hello world\n')
    f.write('haha\n')
    f.seek(0)
    data = f.read()
    print(data)
with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)
with TemporaryDirectory() as dirname:
    print('dirnames is:', dirname)
with NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='c:/downloads/') as f:
    print(f.name)
