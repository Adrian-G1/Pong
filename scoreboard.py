from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.sety(270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"{self.l_score}:{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()
