# 迭代器代替while无限循环
CHUNKSIZE = 8192


def process_data(data):
    pass


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


def reader2(s):
    for chunk in iter(lambda : s.recv(CHUNKSIZE), b''):
        process_data(chunk)


f = open('somefile.txt')
for chunk in iter(lambda : f.read(5), ''):
    print(chunk)