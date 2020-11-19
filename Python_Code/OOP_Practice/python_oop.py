# balance = 0

# def deposit(amount):
#     global balance
#     balance += amount
#     return balance

# def withdraw(amount):
#     global balance
#     balance -= amount
#     return balance

def make_account():
    return {'balance': 0}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

Chase_account = make_account()
BOA_account = make_account()
print(deposit(Chase_account,100))
print(deposit(BOA_account, 50))
print(withdraw(Chase_account,50))
print(withdraw(BOA_account,30))