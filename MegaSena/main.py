'''
Author: Joao Paulo Andrade Pereira
Version: 0.2
Data: 11.07.2019
'''

from MegaSena import last_games
from MegaSena import megasena

qt_dezenas = 7 #Quantidade de dezenas por jogo
qt_jogos = 17 #Quantidade de jogos

if __name__ == '__main__':
    last_games.start()
    for x in range(qt_jogos):
        megasena.gera_jogo_mega_sena(qt_dezenas)