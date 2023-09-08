from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the game window
screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('My Pong Game')
screen.tracer(0)

# Create the right paddle and left paddle
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

# Listen for keyboard events
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# Game state flag
game_on = True

# Create the pong ball
ball = Ball()

scoreboard = Scoreboard()

# Game loop
while game_on:
    # Add a short delay to control the frame rate
    time.sleep(ball.move_speed)

    # Update the game screen
    screen.update()

    # Move the pong ball
    ball.move_ball()

    # Change vertical direction if the ball hits the top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Change horizontal direction if the ball hits a paddle within position range
    if (ball.distance(r_paddle) < 40 and ball.xcor() > 320) or (ball.distance(l_paddle) < 40 and ball.xcor() < -320):
        ball.bounce_x()

    # Reset ball's position if it goes beyond the right edge
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Reset ball's position if it goes beyond the left edge
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
# Click the game window to exit the game
screen.exitonclick()
