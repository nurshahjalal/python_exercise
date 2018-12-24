from inheritence.vehicle import Vehicle


class GasCar(Vehicle):

    def type_of_car(self):
        print("This is Gas car")


gs = GasCar("Ford", "Focus", "2012")
gs.type_of_car()

