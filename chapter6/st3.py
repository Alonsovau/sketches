# 解析简单的xml数据
from urllib.request import urlopen
from urllib import request
from xml.etree.ElementTree import parse


# u = urlopen('http://planetpython.org/rss20.xml')
u = open('rss20.xml','rb')
doc = parse(u)
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link)
u.close()

print(doc)
e = doc.find('channel/title')
print(e)
print(e.tag)
print(e.text)
print(e.get('some_attribute'))