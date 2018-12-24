class Vehicle:

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        print("This is {}, {} of {}".format(self.name, self.model, self.year))


