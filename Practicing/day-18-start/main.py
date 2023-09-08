from turtle import *
import random

colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_return = (r, g, b)
    return random_color_return


timmy = Turtle()
directions = [0, 90, 180, 270]
timmy.width(15)
screen = Screen()
timmy.speed(0)

for _ in range(200):
    timmy.color(random_color())
    timmy.forward(50)
    timmy.setheading(random.choice(directions))

screen.exitonclick()
