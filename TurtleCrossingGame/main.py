import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_turtle, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car_move()

    if player.turtle_finish():
        cars.level_up()
        scoreboard.level_up()

    for car in cars.cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
