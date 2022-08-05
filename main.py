from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.title('PONG')
screen.setup(width=800, height=600)
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkeypress(paddle.go_up, 'Up')
screen.onkeypress(paddle.go_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
