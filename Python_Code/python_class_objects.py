class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def deposit(self, amount):
        self.balance += amount
        return self

    def show_balance(self):
        print(f"Balance: ${self.balance}")
        return self


Chase_account = BankAccount()
BOA_account = BankAccount()

my_transaction = Chase_account.deposit(100).withdraw(30).show_balance()
wife_transaction = BOA_account.deposit(100).withdraw(50).show_balance()