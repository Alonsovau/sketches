# 处理多个异常
import logging
import errno


logger = logging.getLogger()
try:
    f = open('filename')
except OSError as e:
    if e.errno == errno.ENOENT:
        logger.error('File not found')
    elif e.errno == errno.EACCES:
        logger.error('Permission denied')
    else:
        logger.error('Unexpected error: %d', e.errno)
print(FileNotFoundError.__mro__)