from turtle import *
import random

tim = Turtle()
window = Screen()
colormode(255)
tim.speed(0)
tim.width(1)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


for _ in range(60):
    tim.color(random_color())
    tim.circle(100)
    tim.left(6)


window.exitonclick()
