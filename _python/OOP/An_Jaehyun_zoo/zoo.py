class Animal:
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def feed(self):
        self.health_level += 10
        self.happiness_level += 10
        return self

    def display_info(self):
        print(f"Name:{self.name}\nAge:{self.age}\nHealth Level:{self.health_level}\nHappiness Level:{self.happiness_level}")

class Lion(Animal): # child class of Animals' class
    def __init__(self, name, age, health_level, happiness_level, attack_level):
        super().__init__(name, age, health_level, happiness_level)
        self.attack = attack_level

class Tiger(Animal): # child class of Animals' class
    def __init__(self, name, age, health_level, happiness_level, attack_level):
        super().__init__(name, age, health_level, happiness_level)
        self.attack = attack_level

class Bear(Animal): # child class of Animals' class
    def __init__(self, name, age, health_level, happiness_level, attack_level):
        super().__init__(name, age, health_level, happiness_level)
        self.attack = attack_level

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))

    def add_tiger(self, name):
        self.animals.append(Tiger(name))

    def add_bear(self, name):
        self.animals.append(Bear(name))

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
    
lion = Lion("Nala", 4, 100, 100, 120)

print(lion.feed().feed().display_info())
zoo1 = Zoo("Jaehyun's Zoo")
zoo1 = add_lion("Nala")
zoo1.print_all_info()
