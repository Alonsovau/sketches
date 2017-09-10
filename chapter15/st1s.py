from ctypes.util import find_library
import ctypes
import array


print(find_library('m'))
print(find_library('pthread'))

_path = '/usr/lib/libm.dylib'
_mod = ctypes.cdll.LoadLibrary(_path)
# _path是标准库的全路径


# 列表转换ctypes数组
nums = [1, 2, 3]
a = (ctypes.c_double * len(nums))(*nums)
print(a)
print(a[0], a[1])

b = array.array('d', [1, 2, 3])
print(b)
ptr, _ = b.buffer_info()
print(ptr)
print(ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double)))
