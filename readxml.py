import xml.etree.ElementTree as ET
import json
import xmltodict


# tree = ET.ElementTree(file='demo.xml')
# root = tree.getroot()
# mydict = {}
# for child in root.iter():
#     # print(child.tag, child.attrib)
#     mydict = child.attrib
#     mydict[child.tag] = child.text
#     print(mydict)
#     myjson = json.dumps(mydict)
#     with open('demo.json', 'a', encoding='utf-8') as f:
#         f.write(myjson)
f = open('自然人.xml', 'r')
mydict = xmltodict.parse(f.read())
# print(mydict)
# print(json.dumps(mydict, indent=4))
with open('demo.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(mydict, indent=4, ensure_ascii=False))