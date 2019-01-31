import requests as r
import json as j
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

a = {"name": "cef_export", "type": "export_mod", "mispattributes": {"responseType": "application/txt",
"outputFileExtension": "cef"},"meta": {"version": "1", "author": "Hannah Ward",
"description": "Export a module in CEF format", "module-type": ["export"],
"config": ["Default_Severity", "Device_Vendor", "Device_Product", "Device_Version"]}}

def get_data():
    headers = {'Authorization': 'eDDXfKkqW5nFyCFNHXQRRrpj2aAuuqVguqd0bvoK',
               'Accept': 'application/json',
               'Content-Type': 'application/json'}
    data = {"module":"cef_export"}
    dados = r.get('http://misp.brb.com.br/events', headers=headers, verify=False)
    # dados = r.post('http://10.1.16.38/shadow_attributes/index', data=j.dumps(data), headers=headers, verify=False)
    print(dados.json())

def analyze_json():

    file = open('misp.json.ADMIN.json','r',encoding='utf-8').read()
    for x in j.loads(file)['response']:
        print(x)

get_data()