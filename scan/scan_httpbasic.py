import requests
from requests.auth import HTTPBasicAuth
from ipaddress import IPv4Network

class ScanHTTPBasic(object):

    def __init__(self, target_range):
        self.target_range = target_range

    # noinspection PyBroadException
    def search_target(self):
        user = ['root', 'admin']
        password = ['root', 'admin', '123456', '123']
        for ip in IPv4Network(self.target_range):
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

    def search_web_server(self):

        for ip in IPv4Network(self.target_range):
            try:
                print(ip)
                response = requests.get('http://' + str(ip), timeout=5.0, verify=False)
                if str(response.headers['Server']).__contains__('Apache'):
                    f = open('apache_target.txt', 'a+')
                    f.write('IP: {} Server: {} \n'.format(ip, response.headers['Server']))
                    f.close()
                    break

                elif str(response.headers['Server']).__contains__('IIS'):
                    f = open('IIS_target.txt', 'a+')
                    f.write('IP: {} Server: {} \n'.format(ip, response.headers['Server']))
                    f.close()
                    break
                else:
                    f = open('unknow_target.txt', 'a+')
                    f.write('IP: {} Server: {} \n'.format(ip, response.headers['Server']))
                    f.close()
            except requests.exceptions.ConnectionError:
                continue
            except requests.exceptions.ReadTimeout:
                continue
            except Exception:
                continue
