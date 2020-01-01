import sys
import sqlite3


class DatabaseDeleter:
    def __init__(self):
        if sys.platform == 'win32':
            database_path = 'E:/Database/marketdb.db'
        else:
            database_path = '/media/severo/Seagate Expansion Drive/Database/marketdb.db'

        self.conn = sqlite3.connect(database_path)

    def delete(self, info):
        date = info['transaction_date'].split('/')

        year = self.get_year(date)
        if not year:
            raise ValueError('Year not found')

        month = self.get_month(date)
        if not month:
            raise ValueError('Month not found')

        month = month[0][0]
        if info['transaction_type'] == 'purchase':
            self.delete_purchase(info['transaction_name'], info['transaction_value'], date[0], month)

        elif info['transaction_type'] == 'sale':
            self.delete_sale(info['transaction_name'], info['transaction_value'], date[0], month)

        else:
            raise ValueError('Wrong information sent. Check the input formatting method')

    def get_month(self, date):
        month_number = date[1]
        year_number = date[2]
        query = f'SELECT * FROM MONTH_TABLE WHERE month_number={month_number} AND year_number={year_number};'

        cursor = self.conn.cursor()
        cursor.execute(query)

        return cursor.fetchall()

    def get_year(self, date):
        year_number = date[2]
        query = f'SELECT * FROM YEAR_TABLE WHERE year_number={year_number};'

        cursor = self.conn.cursor()
        cursor.execute(query)

        return cursor.fetchall()

    def delete_sale(self, name, value, day, month):
        query = f'DELETE FROM SALE WHERE product_name="{name}" AND value={value} AND day={day} AND id_month={month};'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e

    def delete_purchase(self, name, value, day, month):
        query = f'DELETE FROM PURCHASE WHERE product_name="{name}" AND value={value} AND day={day} AND id_month={month};'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e
