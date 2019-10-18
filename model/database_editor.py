import sqlite3


class DatabaseEditor:
    def __init__(self):
        self.conn = sqlite3.connect('data/marketdb.db')

    def edit(self, info):
        date = info['transaction_date'].split('/')

        year = self.get_year(date)
        if not year:
            return False

        month = self.get_month(date)
        if not month:
            return False

        if info['transaction_type'] == 'purchase':
            result = self.edit_purchase(info['transaction_old_value'], info['transaction_new_value'], date[0], month)

        elif info['transaction_type'] == 'sale':
            result = self.edit_sale(info['transaction_old_value'], info['transaction_new_value'], date[0], month)

        else:
            raise ValueError('Wrong information sent. Check the input formatting method')

        print(result[1])

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

    def edit_sale(self, old_value, new_value, day, month):
        query = f'UPDATE SALE SET value={new_value} WHERE value={old_value} AND day={day} AND id_month={month};'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e

    def edit_purchase(self, old_value, new_value, day, month):
        query = f'UPDATE PURCHASE SET value={new_value} WHERE value={old_value} AND day={day} AND id_month={month};'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e
