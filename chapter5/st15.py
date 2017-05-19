# 打印不合法的文件名
def bad_filename(filename):
    return repr(filename)

try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))