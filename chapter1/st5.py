# 字典排序
from collections import OrderedDict
import json


def order_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])
    d2json = json.dumps(d)
    print(d2json)

order_dict()