# 用cython包装c代码
# 包含文件csample.pxd,sample.pyx
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension(
        'sample',
        ['sample.pyx'],
        libraries=['sample'],
        library_dirs=['.']
    )
]
setup(
    name='Sample extension module',
    cmdclass={'build_ext':build_ext},
    ext_modules=ext_modules
)
# python3 st10.py build_ext --inplace
