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
            self.balace -= 5
            print("insufficient funds: Charing a $5 fee")
        return self

    def display_account_info(self):
        # your code here
        print(f"Balance:${self.balance}")
        return self

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

bank_account1 = BankAccount(int_rate = 0.1, balance=100)
bank_account2 = BankAccount(0.02, 500)

print(bank_account1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info())
print(bank_account2.deposit(50).deposit(150).withdraw(100).withdraw(10).withdraw(40).withdraw(30).yield_interest().display_account_info())