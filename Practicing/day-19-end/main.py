from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtle = []
for index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=-165 + index * 66)
    all_turtle.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_game_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You win, the {win_color} is the winner")
            else:
                print(f"You lost, the {win_color} is the winner")
        rand_dis = random.randint(0, 10)
        turtle.forward(rand_dis)

screen.exitonclick()
