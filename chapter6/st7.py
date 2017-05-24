# 利用命名空间解析xml文档
from xml.etree.ElementTree import parse, iterparse
doc = parse('st7.xml')
print(doc.findtext('author'))
print(doc.find('content'))
print(doc.find('content/html'))
# a query involving a namespace(doesn't work)
print(doc.find('content/{http://www.w3.org/1999/xhtml}html'))
# works
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/title'))
# doesn't work
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/'
                    '{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title'))
# works


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        return path.format_map(self.namespaces)


ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
print(doc.find(ns('content/{html}html')))
print(doc.findtext(ns('content/{html}html/{html}head/{html}title')))

for evt, elem in iterparse('st7.xml', ('end', 'start-ns', 'end-ns')):
    print(evt, elem)
