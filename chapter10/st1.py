# 构建一个模块的层级包
# graphics/
#     __init__.py
#     primitive/
#         __init__.py
#         line.py
#         fill.py
#         text.py
#     formats/
#         __init__.py
#         png.py
#         jpg.py
# import graphics.primitive.line
# from graphics.primitive import line
# import graphics.formats.jpg as jpg
