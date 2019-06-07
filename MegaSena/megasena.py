import database
from random import randint
from last_games import start

start()
numeros_sorteados = []

def gera_numeros_mega_sena(size):
    global numeros_sorteados
    mega = []
    while len(mega) < size:
        number = randint(1,60)
        if (number not in mega) and (number not in numeros_sorteados):
            numeros_sorteados.append(number)
            mega.append(number)
    mega.sort()
    return mega

def gera_numeros_lotofacil(size):
    jogo = []
    while len(jogo) < size:
        number = randint(1,25)
        if number not in jogo:
            jogo.append(number)
    jogo.sort()
    return jogo

def gera_jogo_mega_sena(size=6):
    jogo = gera_numeros_mega_sena(size)
    resposta = 'Jogo válido'
    for x in database.get_data():
        lista = x[1].replace("[","")
        lista = lista.replace("]","")
        lista = lista.split(",")
        match = 0
        for y in range(6):
            if int(lista[y]) in jogo:
                match += 1
        if match == 6:
            resposta = 'Jogo inválido!'
            break
    print(resposta, jogo)
    # statistica = {}
    # statistica_ordenada = {}
    # for i in range(1,61):
    #     quantidade = 0
    #     for x in range(len(resultados)):
    #         if i in resultados[x]:
    #             quantidade += 1
    #     statistica[i] = quantidade
    #     print('O número %i foi sorteado %i vezes.' %(i,quantidade))
    #
    # for k,v in sorted(statistica.items(), key=lambda p:p[1], reverse=True):
    #     statistica_ordenada[k] = v
    #
    # print(statistica_ordenada)


# #Mega Sena
for x in range(2):
    gera_jogo_mega_sena(7)
