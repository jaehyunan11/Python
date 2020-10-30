class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        return (f"User:{self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, transfer_to, amount):
        transfer_to.make_deposit(amount)
        self.make_withdrawal(amount)


user1 = User("Guido", "guido@gmail.com")
user2 = User("Jaehyun", "jaehyun@gmail.com")
user3 = User("Mike", "mike@gmail.com")

user1.make_deposit(100)
user1.make_deposit(100)
user1.make_deposit(100)
user1.make_withdrawal(100)
print(user1.display_user_balance())

user2.make_deposit(100)
user2.make_deposit(100)
user2.make_withdrawal(100)
user2.make_withdrawal(100)
print(user2.display_user_balance())

user3.make_deposit(1000)
user3.make_withdrawal(300)
user3.make_withdrawal(300)
user3.make_withdrawal(300)
print(user3.display_user_balance())

user1.transfer_money(user3, 100)
print(user1.display_user_balance())
print(user3.display_user_balance())