import sqlite3

class DataBase(object):

    def __init__(self, database):
        self.database = database
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()

    def create_database(self):
        try:
            self.cursor.execute('''create table range (id integer not null primary key autoincrement, 
                                range_target text not null unique,
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
            self.cursor.execute("select * from range where scanned = 0 limit 1;")
            data = self.cursor.fetchall()
            return data[0]
        except Exception as e:
            print(e)

    def update_data(self, data):
        try:
            self.cursor.execute("update range set scanned = ? where id = ?;",(1, data[0]))
            self.conn.commit()
        except Exception as e:
            print(e)
    def close_connection(self):
        try:
            self.conn.close()
            self.cursor.close()
        except Exception as e:
            print(e)
    def __delete__(self, instance):
        self.conn.close()
        self.cursor.close()
        print('Instancia deletada')
# c = DataBase('lacnic.db')
# c.create_database()
# c.insert_data('200.11.19.0/24')
# c.update_data(c.get_data())
# print(c.get_data())
