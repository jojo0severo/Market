import sqlite3


class DatabaseSaleRecover:
    def __init__(self):
        self.conn = sqlite3.connect('data/marketdb.db')

    def get_sales(self, from_date, to_date):
        query = """
            SELECT SALE.product_name, SALE.value, SALE.day, MONTH_TABLE.month_number, YEAR_TABLE.year_number 
	            FROM SALE 
		            INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                    INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
	            WHERE
                    MONTH_TABLE.month_number >= {} AND MONTH_TABLE.month_number <= {} AND
                    YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {}
	            ORDER BY
	                YEAR_TABLE.year_number,
		            MONTH_TABLE.month_number,
		            SALE.day;
        """.format(from_date[1], to_date[1], from_date[2], to_date[2])

        cursor = self.conn.cursor()
        resp = cursor.execute(query).fetchall()
        return resp

    def get_total_sales(self, from_date, to_date):
        query = """
                    SELECT SUM(SALE.value)
        	            FROM SALE 
        		            INNER JOIN MONTH_TABLE ON SALE.id_month = MONTH_TABLE.id_month 
                            INNER JOIN YEAR_TABLE ON YEAR_TABLE.year_number = MONTH_TABLE.year_number
        	            WHERE
                            MONTH_TABLE.month_number >= {} AND MONTH_TABLE.month_number <= {} AND
                            YEAR_TABLE.year_number >= {} AND YEAR_TABLE.year_number <= {};
                """.format(from_date[1], to_date[1], from_date[2], to_date[2])

        cursor = self.conn.cursor()
        resp = cursor.execute(query).fetchall()

        return resp[0]

