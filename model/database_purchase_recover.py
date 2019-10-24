import sqlite3


class DatabasePurchaseRecover:
    def __init__(self):
        self.conn = sqlite3.connect('data/marketdb.db')

    def get_purchases(self, from_date, to_date):
        query = """
            SELECT PURCHASE.product_name, PURCHASE.value, PURCHASE.day, MONTH_TABLE.month_number, YEAR_TABLE.year_number 
	            FROM PURCHASE 
		            INNER JOIN MONTH_TABLE ON PURCHASE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
	            WHERE
                    MONTH_TABLE.month_number >= {} AND MONTH_TABLE.month_number <= {} AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {}
	            ORDER BY
		            PURCHASE.day DESC,
		            MONTH_TABLE.month_number DESC;
        """.format(from_date[1], to_date[1], from_date[2], to_date[2])

        cursor = self.conn.cursor()
        resp = cursor.execute(query).fetchall()

        return resp

    def get_total_purchases(self, from_date, to_date):
        query = """
                    SELECT SUM(PURCHASE.value)
                        FROM PURCHASE 
                            INNER JOIN MONTH_TABLE ON PURCHASE.id_month = MONTH_TABLE.id_month 
                            INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
                        WHERE
                            MONTH_TABLE.month_number >= {} AND MONTH_TABLE.month_number <= {} AND
                            YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {};
                """.format(from_date[1], to_date[1], from_date[2], to_date[2])

        cursor = self.conn.cursor()
        resp = cursor.execute(query).fetchall()

        return resp[0]

