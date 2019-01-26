#-*-coding: utf-8-*-

'''
Sequência de parâmetros deve ser respeitada:
usuario | senha | subnet | ip
Python 2
'''

import requests
import urllib3
import getpass
from sys import argv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url_api = 'https://ipamhmo.brb.com.br/api/test/'

def get_id(subnet, token):
    response = requests.get(url_api + 'subnets/all/', headers=token, verify=False)
    lista_subnet = response.json()['data']
    for y, x in enumerate(lista_subnet):
        if x['subnet'] == subnet:
            return (x['id'])

#Convert a mascara do formato CIDR para o formato decimal

def delete_ip():

    if len(argv) == 1:

        usuario = raw_input('Informe o usuário operador para acesso: ')
        senha = getpass.getpass('Informe a senha de acesso para o usuário - '+usuario+': ')
        subnet = raw_input('Informe a sub rede que deseja devolver IP: ')
        ip_del = raw_input('Informe o endereço IP a ser devolvido: ')

    else:

        usuario = argv[1]
        senha = argv[2]
        subnet = str(argv[3])
        ip_del = argv[4]

    try:

        from requests.auth import HTTPBasicAuth
        response = requests.post(url_api + 'user/', auth=HTTPBasicAuth(usuario, senha), verify=False)
        token = {"token": response.json()['data']['token']}
        response = requests.delete(url_api + 'addresses/'+ip_del+'/'+get_id(subnet, token)+'/', headers=token, verify=False)
        return response.json()


    except Exception as e:
        print(e)

delete_ip()
