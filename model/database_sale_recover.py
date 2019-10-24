import sqlite3


class DatabaseSaleRecover:
    def __init__(self):
        self.conn = sqlite3.connect('data/marketdb.db')

    def get_sales(self, from_date, to_date):
        values = [int(item) for tup in zip(from_date, to_date) for item in tup]
        query = """
            SELECT SALE.product_name, SALE.value, SALE.day, MONTH_TABLE.month_number, YEAR_TABLE.year_number 
	            FROM SALE 
		            INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
	            WHERE
                    SALE.day >= {} AND SALE.day <= {} AND
                    MONTH_TABLE.month_number >= {} AND MONTH_TABLE.month_number <= {} AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {}
	            ORDER BY
		            SALE.day DESC,
		            MONTH_TABLE.month_number DESC;
        """.format(*values)

        try:
            cursor = self.conn.cursor()
            resp = cursor.execute(query).fetchall()
            if not resp:
                return [("NaN", 0, 0, 0, 0)]

            return resp

        except sqlite3.OperationalError as e:
            return [("NaN", 0, 0, 0, 0)]

    def get_total_sales(self, from_date, to_date):
        values = [int(item) for tup in zip(from_date, to_date) for item in tup]
        query = """
                    SELECT SUM(SALE.value)
        	            FROM SALE 
        		            INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                            INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
        	            WHERE
                            SALE.day >= {} AND SALE.day <= {} AND
                            MONTH_TABLE.month_number >= {} AND MONTH_TABLE.month_number <= {} AND
                            YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {};
                """.format(*values)

        try:
            cursor = self.conn.cursor()
            resp = cursor.execute(query).fetchall()
            if not resp:
                return -1.1

            return resp[0]

        except sqlite3.OperationalError as e:
            return -1.1
