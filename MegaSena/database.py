import sqlite3

def create_database():
    conn = sqlite3.connect('loterias.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE megasena ( id INTEGER NOT NULL PRIMARY KEY,
    dezenas TEXT NOT NULL);""")
    print('Table criada com sucesso!')
    conn.close()

def insert_data(id, dezenas):
    conn = sqlite3.connect('loterias.db')
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO megasena (id, dezenas)
        VALUES ('{}','{}');""".format(id, dezenas))
        return False
    except sqlite3.IntegrityError as e:
        print('ID já existe!', e)
        return True
    finally:
        conn.commit()
        conn.close()

def get_data():
    conn = sqlite3.connect('loterias.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM megasena;""")
    return cursor.fetchall()
    conn.close()

def info_table():
    conn = sqlite3.connect('workshop.db')
    cursor = conn.cursor()
    cursor.execute('PRAGMA table_info({})'.format('hosts'))
    print('Colunas:')
    for coluna in cursor.fetchall():
        print(coluna)
    cursor.execute("""SELECT name FROM sqlite_master WHERE type = 'table' 
    ORDER BY name;""")
    print('Tabelas:')
    for table in cursor.fetchall():
        print('%s'%(table))
    conn.close()