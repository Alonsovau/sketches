# 增量式解析大型xml文件
from xml.etree.ElementTree import iterparse, parse
from collections import Counter
def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


# potholes_by_zip = Counter()
# doc = parse('potholes.xml')
# for pothhole in doc.iterfind('row/row'):
#     potholes_by_zip[pothhole.findtext('zip')] += 1
# for zipcode, num in potholes_by_zip.most_common():
#     print(zipcode, num)
# 此方法会将整个xml文件加载到内存中然后解析


potholes_by_zip = Counter()
data = parse_and_remove('potholes.xml', 'row/row')
for pothhole in data:
    potholes_by_zip[pothhole.findtext('zip')] += 1
for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)
# 节省内存


data = iterparse('potholes.xml', ('start','end'))
for i in range(7):
    print(next(data))
# start事件在某个元素第一次被创建并且还没有被插入其他数据(如子元素)时被创建。而end事件在某个元素已经完成时被创建。
# 尽管没有在例子中演示， start-ns和end-ns事件被用来处理XML文档命名空间的声明。