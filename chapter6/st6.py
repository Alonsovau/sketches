from xml.etree.ElementTree import parse, Element, tostring
doc = parse('pred.xml')
root = doc.getroot()
print(root)
print(tostring(root))
root.remove(root.find('sri'))
print(tostring(root))
print(root.getchildren().index(root.find('nm')))
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)
print(tostring(root))
doc.write('newpred.xml', xml_declaration=True)