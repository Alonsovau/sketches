# 用cython写高性能的数组操作
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension('sample11', ['sample11.pyx'])
]

setup(
    name='Sample11 app',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
# python3 st11.py build_ext --inplace
