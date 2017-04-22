import sqlite3


class Database:

    DATABASE = 'personalTrainerServer/db/user.db'
    con = None
    cursor = None

    def connect(self):
        self.con = sqlite3.connect(self.DATABASE)
        self.cursor = self.con.cursor()

    def insert(self, table, fields=(), values=()):
        # g.db is the database connection
        msg = []
        try:
            self.connect()
            query = 'INSERT INTO %s (%s) VALUES (%s)' % (
                table,
                ', '.join(fields),
                ', '.join(['?'] * len(values))
            )
            self.cursor.execute(query, values)
            self.con.commit()
            self.con.close()
            msg.append({'message': "Ok", 'code': 200})
            return msg
        except Exception as e:
            print('Database error [{0}]'.format(e.message))
            msg.append({'message': "Error", 'code': 404})
            return msg

    def select(self, query):
        msg = []
        try:
            self.connect()
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.con.close()
            return result
        except Exception as e:
            print('Database error [{0}]'.format(e.message))
            return msg.append({'message': "Error", 'code': 404})
