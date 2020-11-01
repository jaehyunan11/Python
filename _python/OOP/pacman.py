# class Pacman:
#     def __init__(self, color="Yellow"):
#         self.color = color
#         self.name = "Pacman"
#         self.lives = 3


#     def change_color(self, new_color):
#         self.color = new_color # new_color that user input is changed to the new color



# user1 = Pacman("Green")
# print(user1.color)
# user1.color = "Yellow"

class BankAccount:
    def __init__(self, starting_balance, int_rate):
        self.balance = starting_balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
    
    def withdrawl(self, amount):
        self.balance -= amount

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(1000, 0.02)

user1 = User("jaehyun An")
print(user1.account.balance)
user1.account.deposit(500)
print(user1.account.balance)
user1.account.withdrawl(300)
print(user1.account.balance)

print(user1.account.int_rate)