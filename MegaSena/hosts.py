from socket import gethostbyaddr
f = open('ips.txt','r',encoding='utf-8')
for x in f.readlines():
    try:
        print('Host: {} - IP: {}'.format(gethostbyaddr(x.strip())[0],x.strip()))
    except:
        print ('Host: Reverso não configurado - IP: {}'.format(x.strip()))

