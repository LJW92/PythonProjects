# import color gram
# colors = color gram.extract('paint.jpg', 40)
# color = []

import random
import turtle as t
import random

color_list = [(1, 9, 30), (229, 235, 242), (121, 95, 41),
              (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170),
              (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147),
              (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164),
              (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (70, 70, 45),
              (185, 190, 201), (126, 225, 231), (88, 49, 45), (61, 65, 66)]

t.colormode(255)
tim = t.Turtle()
tim.speed(0)

screen = t.Screen()
screen.setup(900, 900)


def go_to_start_point(i):
    tim.penup()
    tim.hideturtle()
    tim.goto(-416, -427.5 + 90 * i)
    tim.pendown()


def draw_filled_circle():
    color = random.choice(color_list)
    tim.dot(25, color)


for i in range(10):
    go_to_start_point(i)
    for j in range(10):
        draw_filled_circle()
        tim.penup()
        tim.forward(90)
        tim.pendown()

screen.exitonclick()
