import random

class Store:
    def __init__ (self, name):
        self.name = name
        self.products = []
        self.product_id = 0

    def add_product(self, name, price, category):
        self.products.append(Product(name, price, category)) 
        self.product_id += 1
        return self

    def sell_product(self, product_id):
        del self.products[product_id]
        print(self.products[product_id])
        return self

    def change_price(self, name, percent_change, is_increased):
        for product in self.products:
            if product.item_name == name:
                product.update_price(percent_change, is_increased)

    def product_info(self, name):
        for product in self.products:
            if product.item_name == name:
                product.print_info()

    def inflation(self, name, percent_increase):
        for product in self.products:
            if product.item_name == name:
                product.update_price(percent_increase, True)

    def set_clearence(self, category, percent_increase):
        for product in self.products:
            if product.item_category == category:
                product.update_price(percent_increase, False)
class Product:
    def __init__ (self, name, price, category):
            self.item_name = name 
            self.item_price = price
            self.item_category = category

    def update_price (self, percent_change, is_increased):
        if is_increased == True:
            self.item_price += self.item_price * percent_change
            return self
        else:
            self.item_price -= self.item_price * percent_change
            return self

    def print_info(self):
        print(self.item_name, self.item_price, self.item_category)
        return self

Supermart = Store("STORE")
Supermart.add_product('orange', 5, 'produce').product_info('orange')
Supermart.sell_product().product_info('orange')
# Supermart.sell_product()
# Supermart.product_info('orange')
# Supermart.set_clearence('produce', .05)
# Supermart.product_info('orange')