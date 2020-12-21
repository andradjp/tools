'''
Author: Joao Paulo Andrade Pereira
Version: 0.2
Data: 11.07.2019
'''

from last_games import LastGames
from megasena import GenerateGames

qt_dezenas = 8 #Quantidade de dezenas por jogo
qt_jogos = 2 #Quantidade de jogos
l = LastGames()
m = GenerateGames()
if __name__ == '__main__':
    print('Quantidade de jogos: {}'.format(qt_jogos))
    print('Dezenas por jogo: {}'.format(qt_dezenas))
    l.start()
    for x in range(qt_jogos):
        m.gera_jogo_mega_sena(qt_dezenas)
    exit()