# 创建和解压归档文件
import shutil


shutil.unpack_archive('python.tgz')
shutil.make_archive('st77', 'zip', '.././chapter1')
print(shutil.get_archive_formats())
