# 将函数指针转换为可调用对象
import ctypes


lib = ctypes.cdll.LoadLibrary(None)
addr = ctypes.cast(lib.sin, ctypes.c_void_p).value
print(addr)

functype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
func = functype(addr)
print(func)

print(func(2))
print(func(0))
