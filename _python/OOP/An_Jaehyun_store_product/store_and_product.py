class Store:
    def __init__(self, name):
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

    # def product_info(self, name):
    def product_info(self):
        for product in self.products:
            product.print_info()
            # if product.item_name == name:  #This code is used to printout specific product_info 
            #     product.print_info()

    def inflation(self, name, percent_increase):
        for product in self.products:
            if product.item_name == name:
                product.update_price(percent_increase, True)

    def set_clearence(self, category, percent_increase):
        for product in self.products:
            if product.item_category == category:
                product.update_price(percent_increase, False)

class Product:
    def __init__(self, name, price, category):
        self.item_name = name
        self.item_price = price
        self.item_category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.item_price += self.item_price * percent_change
            return self
        else:
            self.item_price -= self.item_price * percent_change
            return self

    def print_info(self):
        print(f"Item: {self.item_name}\nPrice: ${self.item_price}\nCategory: {self.item_category}")
        return self

Supermart = Store("STORE")
Supermart.add_product('orange', 5, 'produce')
Supermart.add_product('apple', 10, 'produce')
Supermart.add_product('peach', 4, 'produce' )
Supermart.inflation('orange',0.1)
Supermart.sell_product(1)
Supermart.product_info()












# import random

# class Store:
#     def __init__(self, store_name):
#         self.store_name = store_name
#         self.list_product = []
    
#     def show_products(self):
#         for product in self.list_product:
#             product.print_info()

#     def add_product(self, new_product):
#         self.list_product.append(new_product)
#         return self

#     def sell_product(self, id):
#         self.list_product.pop(id)  # id refers to index
#         return self

#     def inflation(self, percent_increase):
#         for product in self.list_product:
#             product.update_price(percent_increase, True)
#         return self

#     def set_clearance(self, category, percent_discount):
#         for product in self.list_product:
#             if product.product_category == category:
#                 product.update_price(percent_discount,False)
#         return self

# class Product:
#     def __init__(self, product_name, product_price, product_category):
#         self.product_name = product_name
#         self.product_price = product_price
#         self.product_category = product_category
#         # self.product_id = random.randint(1,50)

#     def update_price(self, percent_change, is_increased):
#         if is_increased == True:
#             self.product_price = self.product_price + (self.product_price * percent_change)
#             return self
#         else:
#             self.product_price = self.product_price - (self.product_price * percent_change)
#         return self
            
#     def print_info(self):
#         print(f"Product: {self.product_name}\nCatergory: {self.product_category}\nPrice: {self.product_price}")
#         return self

# product1 = Product("Coffee", 5, "beverages") #instance1
# product2 = Product("TV", 500, "electronics") #instance2

# store = Store("target")
# store.add_product(product1).show_products()
# store.set_clearance("beverage", 0.5).show_products()