from turtle import Turtle, width

WIDTH = 5
HEIGTH = 1
X_POSITION = 350

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGTH)
        self.goto(x=X_POSITION, y=0)

    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)