class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.list_product = []
    
    def show_products(self):
        for product in self.list_product:
            product.print_info()

    def add_product(self, new_product):
        self.list_product.append(new_product)
        return self

    def sell_product(self, id):
        self.list_product.pop(id)  # id refers to index
        return self

    def inflation(self, percent_increase):
        for product in self.list_product:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.list_product:
            if self.list_product[category] == category:
                product.update_price(percent_discount, False)
        return self

class Product:
    def __init__(self, product_name, product_price, product_category):
        self.product_name = product_name
        self.product_price = product_price
        self.product_category = product_category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.product_price = self.product_price + (self.product_price * percent_change)
        else:
            self.product_price = self.product_price - (self.product_price * percent_change)
        return self
            
    def print_info(self):
        print(f"Product: {self.product_name}\nCatergory: {self.product_category}\nPrice: {self.product_price}")
        return self

product1 = Product("Coffee", 5, "beverages") #instance1
product2 = Product("TV", 500, "electronics") #instance2


store = Store("target")
# store.add_product(product2)
# store.show_products()
store.add_product(product1)
store.add_product(product2).show_products()
store.set_clearance("beverage", 0.5).show_products()
# store.add_product(product1).inflation(0.1).set_clearance("beverages",0.5).show_products()
# store.add_product(product2).set_clearance("electronics", 0.5).show_products()
# store.show_products()
# store.sell_product(1)
# store.show_products()



# store.add_product(product2)
# store.show_products()
# store.inflation(0.1)
# store.show_products()
# store.sell_product()
# store.show_products()

# print(product1.print_info())
# print(product1.update_price(0.1, True))
# print(product1.print_info())

# print(product2.print_info())
# print(product2.update_price(0.5, False))
# print(product2.print_info())



# storage = [
#     {'product_name' : 'water', 'product_price' : 5, 'product_catergory': 'beverages'},
#     {'product_name' : 'TV', 'product_price' : 1000, 'product_catergory': 'electronics'}
# ]

# for idx in range(len(storage)):
#     print(storage[idx])
#     for key,val in storage[idx].items():
#         print(key,'-',storage[idx][key])
#         print(val)

# walmart = Store("walmart")
# print(walmart




# walmart = Store("walmart", products)