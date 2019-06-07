import random

def gera_lista():

    lista = []

    for y in range(0, 7):
        number = random.randint(1, 60)
        if number not in lista:
            lista.append(number)
        else:
            pass
        lista.sort()
    print(lista)

gera_lista()
