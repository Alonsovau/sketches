# 简单的c扩展模块
from distutils.core import setup, Extension


setup(name='sam',
      ext_modules=[
          Extension(
              'sam',
              ['sam.c'],
              include_dirs=['/Users/zhouxin/PycharmProjects/sketches/chapter15／'],
              define_macros=[('FOO', '1')],
              undef_macros=['BAR'],
              library_dirs=['/usr/local/lib'],
              libraries=['sam']
          )
      ]
)
# python3 st2.py build_ext --inplace
