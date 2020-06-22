import ipaddress
a = ipaddress.ip_address('127.0.0.1').is_loopback
interface = ipaddress.IPv4Interface('192.0.2.1/32')
print(interface.ip)
print(a)
