# 可以接受任意数量参数的函数
import html


def avg(first, *rest):
    return (first + sum(rest)) / (1+ len(rest))
print(avg(1, 2))
print(avg(1, 2, 3, 4))


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    keyvals2 = [' {}="{}"'.format(item[0], item[1]) for item in attrs.items()]
    print(keyvals)
    print(keyvals2)
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element
print(make_element('item', 'Albatross', size='large', quantity=6))


