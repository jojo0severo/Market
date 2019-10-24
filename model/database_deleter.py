import sqlite3


class DatabaseDeleter:
    def __init__(self):
        self.conn = sqlite3.connect('data/marketdb.db')

    def delete(self, info):
        date = info['transaction_date'].split('/')

        year = self.get_year(date)
        if not year:
            return False

        month = self.get_month(date)
        if not month:
            return False

        month = month[0][0]
        if info['transaction_type'] == 'purchase':
            result = self.delete_purchase(info['transaction_value'], date[0], month)

        elif info['transaction_type'] == 'sale':
            result = self.delete_sale(info['transaction_value'], date[0], month)

        else:
            raise ValueError('Wrong information sent. Check the input formatting method')

        return result[0]

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

    def delete_sale(self, value, day, month):
        query = f'DELETE FROM SALE WHERE value={value} AND day={day} AND id_month={month};'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e

    def delete_purchase(self, value, day, month):
        query = f'DELETE FROM PURCHASE WHERE value={value} AND day={day} AND id_month={month};'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e
