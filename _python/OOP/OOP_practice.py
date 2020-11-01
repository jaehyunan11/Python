from file import Car
# import file


# Defining class and creating instance 

class User: # what holds all the details we want our object instances to have, # Convention of naming is Upper camel case  in first letter
    def __init__(self, name, age, color, email): #init is the function to make an instance, (constructor method)
        self.name = name  #Attribute (some data)
        self.age = age
        self.fav_color = color
        self.email = email
        self.friends = []
        self.my_car = Car(2006, "Honda Civic", "Navy Blue", False)

    def birthday(self): # Method or class functionality
        self.age = self.age + 1
        print(f"Happy Birthday, {self.name}!")
        return self # you can chain methods together if you get back the full instance at the end of the method

    def make_friends(self, other_user):
        self.friends.append(other_user.name)
        other_user.friends.append(self.name)
        print(f"Congrats on your friendship, {self.name} and {other_user.name}")
        return self

# class Car:
#     def __init__(self, year, model, color, nice):
#         self.year = year
#         self.model = model
#         self.color = color
#         self.tricked_out = nice

# car1 = Car(2018, "Hyundai Elantra", "red", False)
# car2 = Car(2017, "GMC Canyon", "black", True)


Amanda = User("Amanda", 30, "Purple", "jaehyuna11@gmail.com") # "Amanda" is a instance of a class
# print(Amanda.name)
# print(Amanda.age)
# print(Amanda.fav_color)
# print(Amanda.email)
print(Amanda.my_car.year)
print(Amanda.my_car.model)
print(Amanda.my_car.tricked_out)

Amanda.birthday().birthday().birthday()
print(Amanda.age)
Judith = User("judith", 30, "rainbow", "asdsd@gmail.com")
Bill = User("Bill", 30, "Periwinkle", "dkfdsf@gmail.com")
Adrian = User("adrian", 28, "Pink", "dfjd11sf@gmail.com")

Amanda.make_friends(Judith).make_friends(Bill).make_friends(Adrian)
print(Amanda.friends)
Amanda.my_car.sweet_ride()
print(Amanda.my_car.tricked_out)

# Judith = User("Judith", 31, "Blue", "asb@gmail.com", car2)
# print(Judith.name)
# print(Judith.age)
# print(Judith.fav_color)
# print(Judith.email)
# print(Judith.friends)
# print(Judith.make_friends(Amanda))

# print(Amanda.birthday())
# print(Amanda.make_friends(Judith))