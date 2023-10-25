import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Breakout")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(5)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5

# Bricks
bricks = []

colors = ["red", "orange", "yellow", "green", "blue"]
for i in range(5):
    for j in range(9):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[i])
        brick.shapesize(stretch_wid=1, stretch_len=3.8)
        brick.penup()
        x = -320 + j * 80
        y = 250 - i * 25
        brick.goto(x, y)
        bricks.append(brick)

# Score and lives
score = 0
lives = 5  # Starting number of lives
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score} Lives: {lives}", align="center", font=("Courier", 24, "normal"))


# Paddle movement
def move_left():
    x = paddle.xcor()
    if x > -360:
        x -= 30
    paddle.setx(x)


def move_right():
    x = paddle.xcor()
    if x < 360:
        x += 30
    paddle.setx(x)


# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")


# Update the score display
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score} Lives: {lives}", align="center", font=("Courier", 24, "normal"))


# Main game loop
pass_check = 0
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        # Player loses a life when the ball drops
        lives -= 1
        update_score()

        # Check for game over
        if lives == 0:
            paddle.hideturtle()
            ball.hideturtle()
            wn.bgcolor("red")
            score_display.clear()
            score_display.goto(0, 0)
            score_display.write("Game Over", align="center", font=("Courier", 36, "normal"))
            wn.update()
            wn.update()
            turtle.done()  # Pause the game
            break  # Exit the game loop

    pass_check -= 1
    if pass_check <= 0:
        pass_check = 0

    # Paddle and ball collisions
    if pass_check == 0:
        if (ball.dx > 0) and (paddle.xcor() + 25 > ball.xcor() > paddle.xcor() - 25) and (-250 < ball.ycor() < -240):
            ball.dy *= -1
            pass_check = 150

        if (ball.dx < 0) and (paddle.xcor() + 25 > ball.xcor() > paddle.xcor() - 25) and (-250 < ball.ycor() < -240):
            ball.dy *= -1
            pass_check = 150

    # Ball and brick collisions
    for brick in bricks:
        if brick is not None and brick.distance(ball) < 30:
            brick.hideturtle()
            bricks.remove(brick)
            ball.dy *= -1
            score += 10
            update_score()

    # Check for win
    if not bricks:
        paddle.hideturtle()
        ball.hideturtle()
        wn.bgcolor("green")
        score_display.clear()
        score_display.goto(0, 0)
        score_display.write("You Win!", align="center", font=("Courier", 36, "normal"))
        wn.update()
        wn.update()
        turtle.done()  # Pause the game
        break  # Exit the game loop
