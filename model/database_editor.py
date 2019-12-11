import sqlite3


class DatabaseEditor:
    def __init__(self):
        self.conn = sqlite3.connect('data/marketdb.db')

    def edit(self, old_info, new_info):
        year = self.get_year(old_info['transaction_date'])
        if not year:
            raise ValueError('Year not found')

        month = self.get_month(old_info['transaction_date'])
        if not month:
            raise ValueError('Month not found')

        month = month[0][0]
        if old_info['transaction_type'] == 'purchase':
            self.edit_purchase(old_info, new_info, month)

        elif old_info['transaction_type'] == 'sale':
            self.edit_sale(old_info, new_info, month)

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

    def insert_year(self, date):
        year_number = date[2]
        query = f'INSERT INTO YEAR_TABLE (year_number) VALUES ("{year_number}");'

        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()

    def insert_month(self, date):
        month_number = date[1]
        year_number = date[2]

        query = f'INSERT INTO MONTH_TABLE (month_number, year_number) VALUES ("{month_number}", "{year_number}");'

        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()

    def edit_sale(self, old_info, new_info, month):
        old_name = old_info['transaction_name']
        old_value = old_info['transaction_value']
        old_day = old_info['transaction_date'][0]
        old_year = old_info['transaction_date'][2]

        cursor = self.conn.cursor()

        get_query = f'SELECT id_sale FROM SALE ' \
                    f'INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month ' \
                    f'WHERE SALE.product_name="{old_name}" AND SALE.value={old_value} AND SALE.day={old_day} ' \
                    f'AND MONTH_TABLE.id_month={month} AND MONTH_TABLE.year_number = {old_year};'
        resp = cursor.execute(get_query).fetchall()

        id_sale = resp[0][0]

        new_name = new_info['transaction_name']
        new_value = new_info['transaction_value']
        new_date = new_info['transaction_date']

        year = self.get_year(new_date)
        if not year:
            self.insert_year(new_date)

        month = self.get_month(new_date)
        if not month:
            self.insert_month(new_date)
            month = self.get_month(new_date)

        month = month[0][0]
        update_query = f'UPDATE SALE SET product_name="{new_name}", value={new_value}, day={new_date[0]}, id_month={month} WHERE id_sale={id_sale};'
        cursor.execute(update_query)
        self.conn.commit()

    def edit_purchase(self, old_info, new_info, month):
        old_name = old_info['transaction_name']
        old_value = old_info['transaction_value']
        old_day = old_info['transaction_date'][0]
        old_year = old_info['transaction_date'][2]

        cursor = self.conn.cursor()

        get_query = f'SELECT id_purchase FROM PURCHASE ' \
                    f'INNER JOIN MONTH_TABLE ON PURCHASE.id_month = MONTH_TABLE.id_month ' \
                    f'WHERE PURCHASE.product_name="{old_name}" AND PURCHASE.value={old_value} AND PURCHASE.day={old_day} ' \
                    f'AND MONTH_TABLE.id_month={month} AND MONTH_TABLE.year_number = {old_year};'

        resp = cursor.execute(get_query).fetchall()

        id_purchase = resp[0][0]
        new_name = new_info['transaction_name']
        new_value = new_info['transaction_value']
        new_date = new_info['transaction_date']

        year = self.get_year(new_date)
        if not year:
            self.insert_year(new_date)

        month = self.get_month(new_date)
        if not month:
            self.insert_month(new_date)
            month = self.get_month(new_date)

        month = month[0][0]
        update_query = f'UPDATE PURCHASE SET product_name="{new_name}", value={new_value}, day={new_date[0]}, id_month={month} WHERE id_purchase={id_purchase};'
        cursor.execute(update_query)
        self.conn.commit()
