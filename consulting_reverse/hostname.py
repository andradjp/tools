import socket

def get_hostname_from_ip():
    f = open('ip_list.txt', 'r')
    ip_list = f.readlines()
    f.close()
    ip = [x.split() for x in ip_list]
    f = open('host_list.txt','w+')
    for x in ip: f.writelines(str(socket.gethostbyaddr(x[1])[0]+'\n'))
    # print(ip_list)
    # reverso = socket.gethostbyaddr(ip)
    # print(reverso[0])
get_hostname_from_ip()