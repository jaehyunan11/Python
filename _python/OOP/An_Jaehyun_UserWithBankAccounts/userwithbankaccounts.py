class User:
    def __init__(self, username):
        self.name = username
        self.account = BankAccount(username)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("insufficient funds: Charing a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

mark = User("Mark")
print(mark.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(300).display_user_balance())