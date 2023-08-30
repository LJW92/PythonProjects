from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.create_cars()
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_cars(self):
        for _ in range(20):
            new_car = Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.speed('fastest')
            start_x = random.randint(-250, 310)
            start_y = random.randint(-250, 250)
            new_car.goto(start_x, start_y)
            new_car.setheading(180)
            self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.forward(self.move_distance)
            if car.xcor() < -320:
                new_y = random.randint(-250, 270)
                new_x = car.xcor() + 630
                car.goto(new_x, new_y)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
