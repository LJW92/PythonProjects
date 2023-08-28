from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.speed('fastest')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.show_score()

    def show_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def got_food(self):
        self.clear()
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
