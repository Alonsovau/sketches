# 复制或者移动文件夹和目录
import shutil

src = ''
dst = ''
shutil.copy(src, dst)
# cp src dst
shutil.copy2(src, dst)
# cp -p src dst
shutil.copytree(str, dst)
# cp -R src dst
shutil.move(src, dst)
# mv src dst
shutil.copytree(src, dst, symlinks=True)
# 只想复制符号链接本身


def ignore_pyc_files(dirname, filenames):
    return [name for name in filenames if name.endwith('.pyc')]
shutil.copytree(src, dst, ignore=ignore_pyc_files)
# 忽略某些文件和目录
