import sys
import sqlite3


class DatabaseKeys:
    def __init__(self):
        if sys.platform == 'win32':
            database_path = 'E:/Database/webdb.db'
        else:
            database_path = '/media/severo/Seagate Expansion Drive/Database/webdb.db'

        self.conn = sqlite3.connect(database_path)

    def get_username_password(self, enterprise):
        query = f'SELECT username, password FROM USER_KEYS WHERE enterprise="{enterprise}";'

        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchone() or ('Desconhecido', 'Desconhecido')

    def insert_username_password(self, enterprise, username, password):
        query = f'INSERT INTO USER_KEYS VALUES ("{enterprise}", "{username}", "{password}");'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e

    def edit_username_password(self, enterprise, password, username=None):
        if username is not None:
            query = f'UPDATE USER_KEYS SET username="{username}" AND password="{password}" WHERE enterprise="{enterprise}";'
        else:
            query = f'UPDATE USER_KEYS SET password="{password}" WHERE enterprise="{enterprise}";'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e
