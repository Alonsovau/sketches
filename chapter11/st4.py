# 通过CIDR地址生成对应的IP地址集
import ipaddress


net = ipaddress.ip_network('123.45.67.64/27')
print(type(net))
for a in net:
    print(a)
net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
print(type(net6))
for a in net6:
    print(a)
print(net.num_addresses)
print(net[-1])
a = ipaddress.IPv4Address('123.45.67.225')
print(a in net)
inet = ipaddress.ip_interface('123.45.67.73/27')
print(inet.network)
print(inet.ip)