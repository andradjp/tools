import ipaddress
import socket

range = ipaddress.IPv4Network('10.7.0.0/22')
for x in range:
    try:
        print(socket.gethostbyaddr(str(x))[0])
    except socket.herror:
        pass
