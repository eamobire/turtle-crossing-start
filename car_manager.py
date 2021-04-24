from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            y_value = random.randint(-200, 200)
            car.goto(300, y_value)
            self.all_cars.append(car)

    def move(self):
        for cars in self.all_cars:
            cars.backward(self.speed)

    def move_next_level(self):
        self.speed += MOVE_INCREMENT
