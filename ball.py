from turtle import Turtle

STARTING_ANGLE = 45
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.angle = STARTING_ANGLE
        

    def move(self):
        self.setheading(self.angle)
        self.forward(10)

    def bounce(self):
        self.angle = 360 - self.angle