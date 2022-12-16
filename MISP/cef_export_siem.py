import requests as rq
from json import dumps
from datetime import datetime, timedelta
import socket

misperrors = {'error': 'Error'}

moduleinfo = {'version': '1', 'author': 'Joao Paulo Andrade',
              'description': 'Export a module in CEF format to SIEM',
              'module-type': ['export']}

moduleconfig = ["Default_Severity", "Device_Vendor", "Device_Product", "Device_Version"]

host_siem = 'x.x.x.x' #SIEM connector
port_siem = 10515 #UDP port on connector
token = ''

cefmapping = {"ip-src": "src", "ip-dst": "dst", "hostname": "dhost", "domain": "dhost",
              "md5": "fileHash", "sha1": "fileHash", "sha256": "fileHash",
              "url": "request"}

filter = {'timestamp':(datetime.now() - timedelta(hours=1)).timestamp()}
headers = {'Authorization': token, 'Accept': 'application/json',
               'Content-Type': 'application/json'}

mispattributes = {'input': list(cefmapping.keys())}
outputFileExtension = "cef"
responseType = "application/txt"

def get_events_by_time():

    try:
        data = rq.post('http://127.0.0.1/attributes/restSearch/json',data=dumps(filter),headers=headers).json()
        if 'Attribute' in data['response']:
            for x in data['response']['Attribute']:
                export_data(request=x)
        else:
            return False
    except ConnectionError as e:
        print(e)
    except Exception as e:
        print(e)

def send_log(d):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = str(d).encode('ascii')
        sock.sendto(data, (host_siem, port_siem))
    except Exception as e:
        print(e)

def export_data(request=False):

    if request is False:
        return False
    if "config" in request:
        config = request["config"]
    else:
        config = {"Default_Severity": 1, "Device_Vendor": "MISP", "Device_Product": "MISP", "Device_Version": 1,
                  'custom1':'deviceCustomDate1'}
        if request["type"] in cefmapping:
            send_log("{} host CEF:0|{}|{}|{}|{}|{}|{}|{}={} {}={}\n".format(
                datetime.now().strftime("%b %d %H:%M:%S"),
                config["Device_Vendor"],
                config["Device_Product"],
                config["Device_Version"],
                request["category"],
                request["category"],
                config["Default_Severity"],
                cefmapping[request["type"]],
                request["value"],
                config["custom1"],
                datetime.fromtimestamp(int(request["timestamp"])).strftime("%b %d %H:%M:%S"),
            ))

get_events_by_time()
