import logging
import chapter13.somelib


logging.basicConfig(level=logging.ERROR)
chapter13.somelib.func()

logging.getLogger('chapter13.somelib').level=logging.DEBUG
chapter13.somelib.func()
# 此段只改变somelib的日志级别
