from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.speed('fastest')
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.show_level()
