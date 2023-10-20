import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Create the bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for i in range(5):
    brick_row = []
    for j in range(-4, 5):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[i])
        brick.shapesize(stretch_wid=1, stretch_len=4)
        brick.penup()
        brick.goto(j * 70, 200 - i * 30)
        brick_row.append(brick)
    bricks.append(brick_row)

# Set up the score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Set up the lives
lives = 3
lives_pen = turtle.Turtle()
lives_pen.speed(0)
lives_pen.color("white")
lives_pen.penup()
lives_pen.hideturtle()
lives_pen.goto(-250, 260)
lives_pen.write(f"Lives: {lives}", align="left", font=("Courier", 24, "normal"))

# Define the paddle movement
def move_left():
    x = paddle.xcor()
    if x > -240:
        x -= 20
    paddle.setx(x)

def move_right():
    x = paddle.xcor()
    if x < 240:
        x += 20
    paddle.setx(x)

# Bind the paddle movement to the arrow keys
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for wall collisions
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        lives -= 1
        lives_pen.clear()
        lives_pen.write(f"Lives: {lives}", align="left", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = 3
        ball.dy = 3

    # Check for paddle collision
    if ball.ycor() < -240 and ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50:
        ball.dy *= -1

    # Check for brick collision
    for i in range(5):
        for j in range(9):
            brick = bricks[i][j]
            if brick is not None and ball.distance(brick) < 40:
                brick.goto(1000, 1000)
                bricks[i][j] = None
                ball.dy *= -1
                score += 10
                score_pen.clear()
                score_pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # Check for game over
    if lives == 0:
        score_pen.goto(0, 0)
        score_pen.write("Game Over", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        screen.bye()

    # Check for level complete
    level_complete = True
    for i in range(5):
        for j in range(9):
            if bricks[i][j] is not None:
                level_complete = False
    if level_complete:
        score_pen.goto(0, 0)
        score_pen.write("Level Complete", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        for i in range(5):
            for j in range(9):
                brick = bricks[i][j]
                brick.goto(j * 70, 200 - i * 30)
                brick.showturtle()
        ball.goto(0, 0)
        ball.dx = 3
        ball.dy = 3
        lives += 1
        lives_pen.clear()
        lives_pen.write(f"Lives: {lives}", align="left", font=("Courier", 24, "normal"))

    # Update the screen
    screen.update()