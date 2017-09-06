# 输出警告信息
import warnings


def func(x, y, logfile=None, debug=False):
    if logfile is not None:
        warnings.warn('logfile argument deprecated', DeprecationWarning)
# python3 -W all st11.py
# python3 -W error st11.py
