from collections import OrderedDict
from model.database_purchase_recover import DatabasePurchaseRecover
from model.database_sale_recover import DatabaseSaleRecover


class GraphicController:
    def __init__(self):
        self.purchase_recover = DatabasePurchaseRecover()
        self.sale_recover = DatabaseSaleRecover()
        self.months = {1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
                       7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'}

    def get_purchases(self, from_date, to_date):
        purchases = self.purchase_recover.get_purchases(from_date.split('/'), to_date.split('/'))
        return True, [tuple([item[0], item[1], item[2:]]) for item in purchases], ''

    def get_sales(self, from_date, to_date):
        sales = self.sale_recover.get_sales(from_date.split('/'), to_date.split('/'))
        return True, [tuple([item[0], item[1], item[2:]]) for item in sales], ''

    def get_purchases_by_date(self, from_date, to_date):
        try:
            result, purchases, message = self.get_purchases(from_date, to_date)
            if not result:
                return False, None, None, message

            dates, values = self.get_dates([item[2] for item in purchases], [item[1] for item in purchases])

            return result, values, dates, message

        except ValueError as e:
            return False, None, None, str(e)

    def get_sales_by_date(self, from_date, to_date):
        try:
            result, sales, message = self.get_sales(from_date, to_date)
            if not result:
                return False, None, None, message

            dates, values = self.get_dates([item[2] for item in sales], [item[1] for item in sales])

            return True, values, dates, ''

        except ValueError as e:
            return False, None, None, str(e)

    def get_profit_by_date(self, from_date, to_date):
        try:
            result, purchases, message = self.get_purchases(from_date, to_date)
            if not result:
                return False, None, None, message

            result, sales, message = self.get_sales(from_date, to_date)
            if not result:
                return False, None, None, message

            purchase_sale_track = {}
            for name, value, date in purchases:
                if date not in purchase_sale_track:
                    purchase_sale_track[date] = -value
                else:
                    purchase_sale_track[date] -= value

            for name, value, date in sales:
                if date not in purchase_sale_track:
                    purchase_sale_track[date] = value
                else:
                    purchase_sale_track[date] += value

            dates = sorted(list(purchase_sale_track.keys()), key=lambda x: (x[2], x[1], x[0]))
            profits = [purchase_sale_track[date] for date in dates]

            dates, values = self.get_dates(dates, profits)

            return True, values, dates, ''

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

    def get_dates(self, dates, values):
        named_dates = []
        if dates[0][1] == dates[-1][1]:
            for date in dates:
                named_dates.append(self.months[int(date[1])] + '/' + str(date[0]))
            return named_dates, values

        month_dict = OrderedDict()
        for idx, date in enumerate(dates):
            if self.months[int(date[1])] not in month_dict:
                month_dict[self.months[int(date[1])]] = values[idx]
            else:
                month_dict[self.months[int(date[1])]] += values[idx]

        return list(month_dict.keys()), list(month_dict.values())
