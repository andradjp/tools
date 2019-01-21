import socket

def get_hostname_from_ip():
    f = open('ip_list.txt', 'r')
    ip_list = f.readlines()
    f.close()
    ip = [x.split() for x in ip_list]
    f = open('host_list.txt','w+')
    z = open('host_unknow.txt','w+')
    for x in ip:
        try:
            f.writelines(str(socket.gethostbyaddr(x[1])[0]+'\n'))
        except socket.herror:
            z.writelines(x)
    f.close()
    z.close()
get_hostname_from_ip()