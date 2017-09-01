# 给函数库增加日志功能
import logging


log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')
