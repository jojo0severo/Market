from model.database_purchase_recover import DatabasePurchaseRecover
from model.database_sale_recover import DatabaseSaleRecover


class GraphicController:
    def __init__(self):
        self.purchase_recover = DatabasePurchaseRecover()
        self.sale_recover = DatabaseSaleRecover()

    def get_purchases_by_month(self, from_date, to_date):
        purchases = self.purchase_recover.get_purchases(from_date.split('/'), to_date.split('/'))
        purchases = [tuple([item[0], item[1], item[2:]]) for item in purchases]
        return purchases, None

    def get_sales_by_month(self, from_date, to_date):
        sales = self.sale_recover.get_sales(from_date.split('/'), to_date.split('/'))
        sales = [tuple([item[0], item[1], item[2:]]) for item in sales]
        return sales, None

    def get_total_purchases(self, from_date, to_date):
        purchases = self.purchase_recover.get_total_purchases(from_date.split('/'), to_date.split('/'))
        return purchases

    def get_total_sales(self, from_date, to_date):
        sales = self.sale_recover.get_total_sales(from_date.split('/'), to_date.split('/'))
        return sales

    def get_profit(self, from_date, to_date):
        purchases = self.purchase_recover.get_total_purchases(from_date.split('/'), to_date.split('/'))
        sales = self.sale_recover.get_total_sales(from_date.split('/'), to_date.split('/'))

        return sales - purchases
