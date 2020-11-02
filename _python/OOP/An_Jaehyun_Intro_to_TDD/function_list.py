def reverseList(list):
    for i in range(int(len(list)/2)):
        list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
    return list

def isPalidrome(list):
    for i in range(int(len(list)/2)):
        if str(list[i]) != str(list[len(list)-i-1]):
            return False
    return True

def coins(amount):
    coin_list = {'quarter' : 25,'dime' : 10,'nickel' : 5, 'penny' : 1}
    change = dict()
    for name, value in coin_list.items():
        change[name], amount = divmod(amount, value)
        if not amount:
            break
    return change


def factorial(num):
    if num < 0:
        return -1
    elif num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
def fibonacci(num):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print(coins(1230))