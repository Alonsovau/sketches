from xml.etree.ElementTree import parse
doc = parse('st7.xml')
print(doc.findtext('author'))
print(doc.find('content'))
print(doc.find('content/html'))
