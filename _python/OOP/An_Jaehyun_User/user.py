class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        return (f"User: {self.name}, Balance: ${self.account_balance}")
    def transfer_money(self, transfer_to, amount):
        self.account_transfer_from = transfer_from
        self.account_transfer_to = transfer_to
        transfer_from = self.account_balance - amount
        transfer_to = self.account_balance + amount
        return(f"User: {self.account_transfer_from}, Balance: {transfer_from}")


user1 = User("Guido")
user2 = User("Jaehyun")
user3 = User("Mike")

user1.make_deposit(100)
user1.make_deposit(100)
user1.make_deposit(100)
user1.make_withdrawal(100)
user2.make_deposit(100)
user2.make_deposit(100)
user2.make_withdrawal(100)
user2.make_withdrawal(100)
user3.make_deposit(1000)
user3.make_withdrawal(300)
user3.make_withdrawal(300)
user3.make_withdrawal(300)


print(user1.display_user_balance())
print(user2.display_user_balance())
print(user3.display_user_balance())
