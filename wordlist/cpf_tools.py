"""
Authon: João Paulo Andrade
Data: 12/05/2018
"""

import random

def gera_cpf():#Função para gerar CPF

    cpf = list(random.choices([0,1,2,3,4,5,6,7,8,9], k=9))#Gera o CPF Aleatório
    #Cálculo do primeiro digito verificador
    pesos = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    primeiro_digito = []
    for idx,i in enumerate(cpf):
        primeiro_digito.append(i * pesos[idx])
    primeiro_digito = sum(primeiro_digito)
    if (primeiro_digito % 11) < 2:
        cpf.append(0)
    else:
        cpf.append(11 - (primeiro_digito % 11))

    #Cálculo do segundo dígito verificador
    pesos = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    segundo_digito = []
    for idx,i in enumerate(cpf):
        segundo_digito.append(i * pesos[idx])
    segundo_digito = sum(segundo_digito)
    if (segundo_digito % 11) < 2:
        cpf.append(0)
    else:
        cpf.append(11 - (segundo_digito % 11))
    return '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*cpf)

def verifica_cpf(cpf):#Função para verificar se o CPF é válido

    cpf = cpf.replace('.','')
    cpf = cpf.replace('-', '')
    cpf = list(map(int, cpf))
    cpf_temp = cpf[0:9]
    pesos = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    primeiro_digito = []
    for idx, i in enumerate(cpf_temp):
        primeiro_digito.append(i * pesos[idx])
    primeiro_digito = sum(primeiro_digito)
    if (primeiro_digito % 11) < 2:
        cpf_temp.append(0)
    else:
        cpf_temp.append(11 - (primeiro_digito % 11))

    pesos = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    segundo_digito = []
    for idx,i in enumerate(cpf_temp):
        segundo_digito.append(i * pesos[idx])
    segundo_digito = sum(segundo_digito)
    if (segundo_digito % 11) < 2:
        cpf_temp.append(0)
    else:
        cpf_temp.append(11 - (segundo_digito % 11))

    if cpf == cpf_temp:
        return 'CPF valido!'
    else:
        return 'CPF invalido'

for x in range(50):
    print(gera_cpf())
