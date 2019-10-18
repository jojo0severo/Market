import sqlite3


class DatabaseRegister:
    def __init__(self):
        self.conn = sqlite3.connect('data/marketdb.db')

    def register(self, info):
        date = info['transaction_date'].split('/')

        year = self.get_year(date)
        if not year:
            self.insert_year(date)

        month = self.get_month(date)
        if not month:
            self.insert_month(date)

        month = self.get_month(date)
        if info['transaction_type'] == 'purchase':
            result = self.insert_purchase(info['product_name'], info['transaction_value'], date[0], month)

        elif info['transaction_type'] == 'sale':
            result = self.insert_sale(info['product_name'], info['transaction_value'], date[0], month)

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

    def insert_year(self, date):
        year_number = date[2]

        query = f'INSERT INTO YEAR_TABLE (year_number) VALUES ("{year_number}");'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e

    def insert_month(self, date):
        month_number = date[1]
        year_number = date[2]

        query = f'INSERT INTO MONTH_TABLE (month_number, year_number) VALUES ("{month_number}", "{year_number}");'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e

    def insert_sale(self, product_name, value, day, month):
        query = f'INSERT INTO SALE (product_name, value, day, id_month) VALUES ("{product_name}", {value}, {day}, {month});'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e

    def insert_purchase(self, product_name, value, day, month):
        query = f'INSERT INTO PURCHASE (product_name, value, day, id_month) VALUES ("{product_name}", {value}, {day}, {month});'

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, None

        except sqlite3.OperationalError as e:
            return False, e
