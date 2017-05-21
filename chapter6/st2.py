# 读取JSON数据
import json
data = {'name': 'ACME',
        'shares': 100,
        'price': 542.23
}
json_str = json.dumps(data)
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


from urllib.request import urlopen
u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
resp = json.loads(u.read().decode('utf-8'))
from pprint import pprint
pprint(resp)


s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict


