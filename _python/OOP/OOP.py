import random

class Game:
    def __init__(self, guess):
        self.guess = guess
        self.rand_number= round(random.random()*10)

    def gameplay(self):
        if self.guess > self.rand_number:
            print("Guess to high")
        elif self.guess < self.rand_number:
            print("Guess to low")
        else:
            print("You Guessed correctly")
        return self

    def change_guess(self, new_guess):
        self.guess = new_guess
        return self

class User:
    def __init__(self, username, guess):
        self.name = username
        self.score = 0
        self.game = Game(guess)

    def greeting(self):
        print(f"Hello from {self.name}")
        return self # object return

    def greeting_another_user(self, another_user):
        print(f"{self.name} says hello to {another_user.name}")
        return self


#instatiating some users

mark = User("Mark",4)
andy = User("Andy",0)
kevin = User("Kevin",4)
hannah = User("hannah",8)

mark.greeting().greeting().greeting_another_user(kevin)
print(mark.game.gameplay().change_guess(4).gameplay())
print(andy.game.gameplay().change_guess(7).gameplay())