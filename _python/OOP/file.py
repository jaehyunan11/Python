class Car:
    def __init__(self, year, model, color, nice):
        self.year = year
        self.model = model
        self.color = color
        self.tricked_out = nice

    def sweet_ride(self):
        self.tricked_out = True
        print("Nice, you tricked out your ride!")