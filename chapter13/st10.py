# 读取配置文件
from configparser import ConfigParser
import sys


cfg = ConfigParser()
print(cfg.read('test.ini'))
print(cfg.sections())
print(cfg.get('installation', 'library'))
print(cfg.getboolean('debug', 'log_errors'))
print(cfg.getint('server', 'port'))
print(cfg.get('server', 'signature'))

cfg.set('server', 'port', '9000')
cfg.set('debug', 'log_errors', 'False')
cfg.write(sys.stdout)


# 读取多个配置文件
print('------')
print(cfg.get('installation', 'prefix'))
cfg.read('test2.ini')
print(cfg.get('installation', 'prefix'))
print(cfg.get('installation', 'library'))
print(cfg.getboolean('debug', 'log_errors'))
