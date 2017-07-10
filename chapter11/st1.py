# 作为客户端与HTTP服务交互
from urllib import request, parse
import requests


url = 'http://httpbin.org/get'
params = {
    'name1': 'value1',
    'name2': 'value2'
}
querystring = parse.urlencode(params)
print(url + '?' + querystring)
u = request.urlopen(url + '?' + querystring)
resp = u.read()


url = 'http://httpbin.org/post'
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()


headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}
req = request.Request(url, querystring.encode('ascii'), headers=headers)
u = request.urlopen(req)
resp = u.read()


r = requests.get('http://httpbin.org/get?name=Dave&n=37',
                 headers = { 'User-agent': 'goaway/1.0'})
resp = r.json()
print(resp['headers'])
print(resp['args'])
