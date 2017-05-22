# 读取JSON数据
import json
data = {'name': 'ACME',
        'shares': 100,
        'price': 542.23
}
json_str = json.dumps(data, indent=4)
print(json_str)
data1 = json.loads(json_str)
print(data1)


with open('data.json', 'w') as f:
    json.dump(data, f)
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)


print(json.dumps(False))
d = {
    'a': True,
    'b': 'Hello',
    'c': None
}
print(json.dumps(d))


# from urllib.request import urlopen
# from pprint import pprint
# try:
#     u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
#     resp = json.loads(u.read().decode('utf-8'))
#     pprint(resp)
# except Exception:
#     pass


s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d
data = json.loads(s, object_hook=JSONObject)
print(data.shares)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(2, 3)
def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d
objdata = json.dumps(p, default=serialize_instance)
print(objdata)
print('-----------------------')
print(json.dumps(p, default=lambda obj: obj.__dict__))  # 匿名函数把实例变量存储在dict中
# 序列化对象实例
classes = {'Point': Point}
def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d
objfromjson = json.loads(objdata, object_hook=unserialize_object)
print(objfromjson, objfromjson.x)
# 反序列化对象实例