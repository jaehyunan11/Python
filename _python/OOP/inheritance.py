class BankAccount: # parent class
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("OMSIFFOCOEMT FUNDS")
        return self

class CheckingAccount(BankAccount): # child class
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount) # attributes that contain in parent(BankAccount) class
        # if (self.balance - amount) > 0:
        #     self.balance -= amount
        # else:
        #     print("INSUFFICIENT FUNDS")
        return self

    def write_check(self, amount):
        pass

    def diplay_account_info(self):
        pass

class RetirementAccount(BankAccount): # child class
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance) # attributes that contain in parent class
        self.is_roth = is_roth

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def display_account_info(self):
        pass

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = CheckingAccount(0.1, 100)

    def make_deposit(self, amount):
        self.account.deposit(100)

user1 = User("Jaehyun", "jaehyuna11@gmail.com")

print(f"Before my balanace was {user1.account.balance}")