from turtle import Turtle
from scoreboard import Scoreboard

STARTING_ANGLE = 45
STARTING_SPEED = 10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.angle = STARTING_ANGLE
        self.move_speed = STARTING_SPEED
        

    def move(self):
        self.setheading(self.angle)
        self.forward(self.move_speed)

    def bounce_wall(self):
        self.angle = 360 - self.angle

    def bounce_paddle(self):
        self.angle = 180 - self.angle

    def refresh(self):
        self.move_speed = STARTING_SPEED
        self.home()
        if self.heading() == 45 or self.heading() == 315:
            self.angle = 225

    def increase_speed(self):
        self.move_speed += 3.5

    def increase_score(self, x_cor, s: Scoreboard):
        if x_cor > 390:
            s.l_point()
            self.refresh()
        elif x_cor < -390:
            s.r_point()
            self.refresh()
