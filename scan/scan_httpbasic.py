import requests
from requests.auth import HTTPBasicAuth
from ipaddress import IPv4Network
from scan.lib import GetTarget


class ScanHTTPBasic:

    def __init__(self):
        g = GetTarget()

    # noinspection PyBroadException
    @staticmethod
    def search_target(target_range):
        user = ['root', 'admin']
        password = ['root', 'admin', '123456', '123']
        for ip in IPv4Network(target_range):
            print(ip)
            try:
                response = requests.get('http://' + str(ip), timeout=5.0)
                if response.status_code == 401:
                    for u in user:
                        for p in password:
                            response = requests.get('http://'+str(ip), auth=HTTPBasicAuth(u, p))
                            if response.status_code == 200:
                                f = open('target_accessed.txt', 'a+')
                                f.write('IP: {} User: {} Password: {}\n'.format(ip, u, p))
                                f.close()
                                break
            except requests.exceptions.ConnectionError:
                continue
            except requests.exceptions.ReadTimeout:
                continue
            except Exception:
                continue
