"""
Author: Joao Paulo Andrade Pereira
Email: contact@jpandrade.info
Data: 18/01/2021

---Description---
Get name server based on domain list

"""

from whois import whois
from socket import gethostbyname
from time import sleep

class getIpNameServers:

    def __init__(self):
        print('[!]Starting search...')

    def getCompareInfo(self,domain):
        try:
            domain_info = whois(domain)
            print('[+]Searching domain: ' + domain)
            for x in domain_info.name_servers:
                print(gethostbyname(x))
                if gethostbyname(x) == '46.4.124.165':
                    print('[!]Domain Found! ' + x)
                    return True
        except Exception as e:
            print(e)

    def openFile(self):
        domains = []
        f = open('/Users/jpandrade/VSCode/tools/DNS/domains','r')
        for x in f.readlines():
            domains.append(x.replace('\n',''))
        f.close()
        return domains

if __name__ == '__main__':
    init = getIpNameServers()
    domains = init.openFile()
    for x in domains:
        if init.getCompareInfo(x):
            break
        #sleep(1)

