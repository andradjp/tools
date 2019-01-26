import requests
import urllib3
import getpass
from sys import argv
from netaddr import IPNetwork
from requests.auth import HTTPBasicAuth

'''Necessario instalar as bibliotecas: requests e netaddr'''

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url_api = 'https://ipamhmo.brb.com.br/api/test/'

#Funcao que retorna o ID da rede, mascara e gateway
def get_id(subnet, token):
    response = requests.get(url_api + 'subnets/all/', headers=token, verify=False)
    lista_subnet = response.json()['data']
    for y, x in enumerate(lista_subnet):
        if x['subnet'] == subnet:
            return (x['id'], x['mask'], x['gateway']['ip_addr'])

#Convert a mascara do formato CIDR para o formato decimal
def convert_cidr(mask):
    network = '0.0.0.0/{}'.format(mask)
    return str(IPNetwork(network).netmask)

def main(argumentos):

    #Solicita os dados se nenhum arugmento for passado por parametro
    if len(argumentos) == 1:

        usuario = raw_input('Informe o usuario operador para acesso: ')
        senha = getpass.getpass('Informe a senha de acesso para o usuario - ' + usuario + ': ')
        subnet = raw_input('Informe a rede que deseja solicitar IP: ')
        descricao = raw_input('Informe a destinacao do IP (Ambiente e/ou Servico): ').upper()
        hostname = raw_input('Informe o Hostname (Exemplo: SWI340203): ').upper()
        responsavel = raw_input('Informe o nome do Requisitante e NUCLEO (Exemplo: Daniel - NUBAP): ').upper()

    else:
        #Configura os dados passados via argumento
        try:
            usuario = argumentos[1]
            senha = argumentos[2]
            subnet = str(argumentos[3])
            descricao = argumentos[4].upper()
            hostname = argumentos[5].upper()
            responsavel = argumentos[6].upper()
        except IndexError as e:
            print('Argumentos invalidos. {}'.format(e))

    try:
        #Faz logon na aplicacao e gera o token
        response = requests.post(url_api + 'user/', auth=HTTPBasicAuth(usuario, senha),
                                 verify=False)
        token = {"token": response.json()['data']['token']}

        address_data = {'description': descricao, 'hostname': hostname, 'owner': responsavel}
        pk = get_id(subnet, token)
        #Requisita o IP
        response = requests.post(url_api + 'addresses/first_free/'+pk[0]+'/',
            headers=token, data=address_data, verify=False)
        print({'IP':str(response.json()['data']), 'MASK':convert_cidr(pk[1]), 'GATEWAY':str(pk[2])})
        return {'IP':str(response.json()['data']), 'MASK':convert_cidr(pk[1]), 'GATEWAY':str(pk[2])}

    except Exception as e:
        print(e)

logon(argv)
