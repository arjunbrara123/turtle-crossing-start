from car import Car
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_CARS = 20


class CarManager:

    def __init__(self):
        super().__init__()
        self.level = 0
        self.cars_on_road = set()

    def move(self, level=0):
        to_remove = set()
        for car in self.cars_on_road:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * level)
            if car.xcor() < -280:
                car.setx(300)
                car.sety(randint(30, 200)*choice([-1, 1]))
                car.color(choice(COLORS))

    def add_car(self):
        if len(self.cars_on_road) < MAX_CARS:
            car = Car(choice(COLORS), randint(30, 200)*choice([-1, 1]))
            self.cars_on_road.add(car)
