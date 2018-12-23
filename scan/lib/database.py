import sqlite3

class DataBase(object):

    def __init__(self, database):
        self.database = database
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()

    def create_database(self):
        try:
            self.cursor.execute('''create table range (id integer not null primary key autoincrement, 
                                range_target text not null,
                                scanned boolean default false)''')
        except Exception as e:
            print(e)

    def insert_data(self, range):

        try:
            self.cursor.execute("insert into range (range_target) values ('%s');"%range)
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_data(self):
        try:
            self.cursor.execute("select * from range where scanned = 'false' limit 1;")
            data = self.cursor.fetchall()
            return data[0]
        except Exception as e:
            print(e)

    def __delete__(self, instance):
        self.cursor.close()
        print('Instancia deletada')
# c = DataBase('lacnic.db')
# c.create_database()
# c.insert_data('200.11.18.0/24')
# c.get_data()
