from urllib import request
import requests


proxy = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080'
}
# proxy_support = request.ProxyHandler({'http': 'http://127.0.0.1:1080'})
# opener = request.build_opener(proxy_support, request.HTTPHandler)
# request.install_opener(opener)
#
# req = request.Request('http://www.instagram.com')
# # req = request.Request('https://www.baidu.com')
# # req.add_header('origin', 'https://www.instagram.com')
# req.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
# # req.add_header('referer', 'https://www.instagram.com/')
# with request.urlopen(req) as f:
#     print(f.read().decode('utf-8'))

url = 'https://www.instagram.com'
# headers = {
#     "Origin": "http://www.instagram.com/",
#     "Referer": "http://www.instagram.com/",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/58.0.3029.110 Safari/537.36",
#     "Host": "www.instagram.com",
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "accept-encoding": "gzip, deflate, sdch, br",
#     "accept-language": "zh-CN,zh;q=0.8",
#     "X-Instragram-AJAX": "1",
#     "X-Requested-With": "XMLHttpRequest",
#     "Upgrade-Insecure-Requests": "1",
# }
res = requests.get(url, proxies=proxy)
print(type(res.content.decode()))
with open('ins.html', 'w') as f:
    f.write(res.content.decode())
