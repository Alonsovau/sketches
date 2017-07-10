import requests


url = 'http://httpbin.org/post'
params = {
    'name1': 'value1',
    'name2': 'value2'
}
headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}
resp = requests.post(url, data=params, headers=headers)
text = resp.text


resp = requests.head('http://www.python.org/index.html')
status = resp.status_code
last_modified = resp.headers['content-length']


# 基本认证登录
resp = requests.get('http://pypi.python.org/pypi?:action=login', auth=('user','password'))


# 将HTTP cookies从一个请求传递到另一个的例子
resp1 = requests.get(url)
resp2 = requests.get(url, cookies=resp1.cookies)


# 上传内容
url = 'http://httpbin.org/post'
files = {'file': ('data.csv', open('data.csv', 'rb'))}
r = requests.post(url, files=files)
