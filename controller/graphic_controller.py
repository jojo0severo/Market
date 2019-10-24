from model.database_purchase_recover import DatabasePurchaseRecover
from model.database_sale_recover import DatabaseSaleRecover


class GraphicController:
    def __init__(self):
        self.purchase_recover = DatabasePurchaseRecover()
        self.sale_recover = DatabaseSaleRecover()
        self.months = {1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
                       7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'}

    def get_purchases_by_month(self, from_date, to_date):
        try:
            months = self.get_months(from_date, to_date)
            purchases = self.purchase_recover.get_purchases(from_date.split('/'), to_date.split('/'))
            purchases = [tuple([item[0], item[1], item[2:]]) for item in purchases]
            return True, purchases, months, ''

        except ValueError as e:
            return False, None, None, str(e)

    def get_sales_by_month(self, from_date, to_date):
        try:
            months = self.get_months(from_date, to_date)
            sales = self.sale_recover.get_sales(from_date.split('/'), to_date.split('/'))
            sales = [tuple([item[0], item[1], item[2:]]) for item in sales]

            return True, sales, months, ''

        except ValueError as e:
            return False, None, None, str(e)

    def get_profit_by_month(self, from_date, to_date):
        try:
            months = self.get_months(from_date, to_date)
            purchases = self.purchase_recover.get_purchases(from_date.split('/'), to_date.split('/'))
            purchases = [item[1] for item in purchases]

            sales = self.sale_recover.get_sales(from_date.split('/'), to_date.split('/'))
            sales = [item[1] for item in sales]

            profits = []
            if len(sales) > len(purchases):
                for sale, purchase in zip(sales[:len(purchases)], purchases):
                    profits.append(sale - purchase)

                for sale in sales[len(purchases):]:
                    profits.append(sale)

            elif len(sales) < len(purchases):
                for purchase, sale in zip(purchases[:len(sales)], sales):
                    profits.append(sale - purchase)

                for purchase in purchases[len(sales):]:
                    profits.append(-purchase)

            else:
                profits = [sale - purchase for sale, purchase in zip(sales, purchases)]

            return True, profits, months, ''

        except ValueError as e:
            return False, None, None, str(e)

    def get_total_purchases(self, from_date, to_date):
        purchases = self.purchase_recover.get_total_purchases(from_date.split('/'), to_date.split('/'))
        return purchases

    def get_total_sales(self, from_date, to_date):
        sales = self.sale_recover.get_total_sales(from_date.split('/'), to_date.split('/'))
        return sales

    def get_total_profit(self, from_date, to_date):
        purchases = self.purchase_recover.get_total_purchases(from_date.split('/'), to_date.split('/'))
        sales = self.sale_recover.get_total_sales(from_date.split('/'), to_date.split('/'))

        return sales - purchases

    def get_months(self, from_date, to_date):
        from_date = from_date.split('/')
        to_date = to_date.split('/')

        months = []
        if from_date[2] < to_date[2]:
            for i in range(int(from_date[1]), 13):
                months.append(self.months[i])

            for i in range(1, int(to_date[1]) + 1):
                months.append(self.months[i])

        elif from_date[2] == to_date[2]:
            for i in range(int(from_date[1]), int(to_date[1]) + 1):
                months.append(self.months[i])

        else:
            raise ValueError('A data de início não pode ser maior do que a data de fim.')

        months.reverse()
        return months
