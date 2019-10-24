import sqlite3


class DatabasePurchaseRecover:
    def __init__(self):
        self.conn = sqlite3.connect('data/marketdb.db')

    def get_purchases(self, from_date, to_date):
        values = [int(item)for tup in zip(from_date, to_date) for item in tup]
        query = """
            SELECT PURCHASE.product_name, PURCHASE.value, PURCHASE.day, MONTH_TABLE.month_number, YEAR_TABLE.year_number 
	            FROM PURCHASE 
		            INNER JOIN MONTH_TABLE ON PURCHASE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
	            WHERE
                    PURCHASE.day >= {} AND PURCHASE.day <= {} AND
                    MONTH_TABLE.month_number >= {} AND MONTH_TABLE.month_number <= {} AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {}
	            ORDER BY
		            PURCHASE.day DESC,
		            MONTH_TABLE.month_number DESC;
        """.format(*values)

        try:
            cursor = self.conn.cursor()
            resp = cursor.execute(query).fetchall()
            if not resp:
                return [("NaN", 0, "NaN")]

            return resp

        except sqlite3.OperationalError:
            return [("NaN", 0, "NaN")]

    def get_total_purchases(self, from_date, to_date):
        values = [int(item) for tup in zip(from_date, to_date) for item in tup]
        query = """
                    SELECT SUM(PURCHASE.value)
                        FROM PURCHASE 
                            INNER JOIN MONTH_TABLE ON PURCHASE.id_month = MONTH_TABLE.id_month 
                            INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                        WHERE
                            PURCHASE.day >= {} AND PURCHASE.day <= {} AND
                            MONTH_TABLE.month_number >= {} AND MONTH_TABLE.month_number <= {} AND
                            YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {};
                """.format(*values)

        try:
            cursor = self.conn.cursor()
            resp = cursor.execute(query).fetchall()
            if not resp:
                return -1.1

            return resp[0]

        except sqlite3.OperationalError:
            return -1.1
