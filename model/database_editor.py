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

        month = month[0][0]

        if info['transaction_type'] == 'purchase':
            self.edit_purchase(info['transaction_old_value'], info['transaction_new_value'], date[0], month)

        elif info['transaction_type'] == 'sale':
            self.edit_sale(info['transaction_old_value'], info['transaction_new_value'], date[0], month)

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

    def edit_sale(self, old_value, new_value, day, month):
        cursor = self.conn.cursor()

        get_query = f'SELECT id_sale FROM SALE WHERE value={old_value} AND day={day} AND id_month={month};'
        resp = cursor.execute(get_query).fetchall()
        if not resp:
            return False, 'Value not found'

        id_sale = resp[0][0]

        update_query = f'UPDATE SALE SET value={new_value} WHERE id_sale={id_sale};'
        cursor.execute(update_query)
        self.conn.commit()

    def edit_purchase(self, old_value, new_value, day, month):
        cursor = self.conn.cursor()

        get_query = f'SELECT id_purchase FROM PURCHASE WHERE value={old_value} AND day={day} AND id_month={month};'
        resp = cursor.execute(get_query).fetchall()
        if not resp:
            return False, 'Value not found'

        id_purchase = resp[0][0]

        update_query = f'UPDATE PURCHASE SET value={new_value} WHERE id_purchase={id_purchase}'
        cursor.execute(update_query)
        self.conn.commit()
