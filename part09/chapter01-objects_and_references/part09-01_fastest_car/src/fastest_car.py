class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

def fastest_car(cars: list):
    speed = 0
    car = ""
    for x in cars:
        if x.top_speed > speed:
            speed = x.top_speed
            car = x.make
    return car