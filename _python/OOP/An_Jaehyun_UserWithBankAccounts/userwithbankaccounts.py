class User:
    def __init__(self, username, bank_name):
        self.name = username
        self.account_num = math.random()
        self.account = BankAccount(username)

    def getAccountNum(self):
        return self.getAccountNum

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
    def __init__(self, int_rate=0, balance=0, account_num=""):
        self.int_rate = int_rate
        self.balance = balance
        self.bank_name = bank_name
        self.account_num = account_num

    def bank_name(self):
        print(f"Bank :{self.bank_name}")
        return self

    def account_num(self):
        print(f"Account number: {self.account_num}")
        return self

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

mark = User("Mark", "Chase")
print(mark.bank_name().make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(300).display_user_balance())