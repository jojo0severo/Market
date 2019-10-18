import sqlite3


class DatabasePasswordRecover:
    def __init__(self):
        self.conn = sqlite3.connect('data/webdb.db')

    def get_username_password(self, enterprise):
        query = f'SELECT username, password FROM USER_KEYS WHERE enterprise="{enterprise}";'

        cursor = self.conn.cursor()
        cursor.execute(query)

        return cursor.fetchall()[0]
