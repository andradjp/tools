import os

lista = open('consulta_ntp.txt','r').readlines()

text = []

def ping(host):
    text = os.popen("ping -c 3 " + host).read().replace('\n','').split(' ')
    for y in text:
        if 'ttl' in y:
            sistema = y.split('=')
            try:
                identifica_sistema(int(sistema[1]), host)
            except:
                pass
            break
    text.clear()
def identifica_sistema(ttl, host):
    if ttl > 250 and ttl <= 255:
        file = open('resultado_unix.txt', 'a', encoding='utf8')
        file.writelines(host+'\n')
        file.close()
    elif ttl > 60 and ttl <= 64:
        file = open('resultado_linux.txt', 'a', encoding='utf8')
        file.writelines(host+'\n')
        file.close()
    elif ttl > 120 and ttl <= 128:
        file = open('resultado_windows.txt', 'a', encoding='utf8')
        file.writelines(host+'\n')
        file.close()

for x in lista:
     ping(x.strip())