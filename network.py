from urllib import request


proxy_support = request.ProxyHandler({'http': 'http://127.0.0.1:1080'})
opener = request.build_opener(proxy_support, request.HTTPHandler)
request.install_opener(opener)

req = request.Request('http://www.instagram.com')
# req = request.Request('https://www.baidu.com')
# req.add_header('origin', 'https://www.instagram.com')
req.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
# req.add_header('referer', 'https://www.instagram.com/')
with request.urlopen(req) as f:
    print(f.read().decode('utf-8'))