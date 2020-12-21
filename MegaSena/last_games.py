from selenium import webdriver
from time import sleep
from pathlib import Path
import database


driver = webdriver.Chrome(executable_path='/Users/jpandrade/VSCode/tools/MegaSena/chromedriver')
driver.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/')

class LastGames:

    def update_database(self):
        db = Path('loterias.db')
        if not db.is_file():
            database.create_database()
        if not database.insert_data(*self.get_jogos()):
            return True
        else:
            print('Banco de dados atualizado!')
            return False

    def get_jogos(self):

        jogo = []

        try:
            concurso = driver.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div/div[3]/section/div[2]/div[2]/div/div[2]/'
                                            'div[1]/div/h2/span').pop().text
            concurso = concurso.split(' ')[1]
            dezenas = driver.find_elements_by_id('ulDezenas').pop().text
            for x in range(0,11,2):
                jogo.append(int('{}{}'.format(dezenas[x],dezenas[x+1])))
            return concurso, jogo
        except Exception as e:
            print(e)

    def start(self):
        while self.update_database():
            driver.find_element_by_link_text('< Anterior').click()
            sleep(1)
        driver.close()
