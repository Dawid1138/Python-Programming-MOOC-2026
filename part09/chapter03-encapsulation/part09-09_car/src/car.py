class Car:
    def __init__(self):
        self.__odometer = 0
        self.__fuel = 0

    def fill_up(self):
        self.__fuel = 60

    def drive(self, km):
        if km <= self.__fuel:
            self.__odometer += km
            self.__fuel -= km
        else:
            self.__odometer += self.__fuel
            self.__fuel = 0

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__fuel} litres"