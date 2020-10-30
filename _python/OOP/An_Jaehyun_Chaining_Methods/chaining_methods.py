class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print (f"User:{self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, transfer_to, amount):
        transfer_to.make_deposit(amount)
        self.make_withdrawal(amount)
        return self

user1 = User("Guido", "guido@gmail.com")
user2 = User("Jaehyun", "jaehyun@gmail.com")
user3 = User("Mike", "mike@gmail.com")

user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
user2.make_deposit(110).make_deposit(250).make_deposit(200).make_withdrawal(530).display_user_balance()
user3.make_deposit(150).make_deposit(230).make_deposit(700).make_withdrawal(510).display_user_balance()
