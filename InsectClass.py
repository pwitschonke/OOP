import random as r

class Insect:

    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = 0

    def length_of_flight(self):
        self.flight = r.randint(1,10)
    
    def get_flight_length(self):
        return self.flight