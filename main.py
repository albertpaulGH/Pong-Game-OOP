# https://docs.python.org/3/library/turtle.html
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
l_score = Scoreboard(-100, 190)
r_score = Scoreboard(100, 190)


screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

game_on = True
delay = 0.1
while game_on:
    time.sleep(delay)
    screen.update()
    ball.move()

    # Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with the paddles
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        delay -= 0.005

    if ball.xcor() > 380:
        ball.reset_position()
        l_score.increment()
        delay = 0.1

    if ball.xcor() < -380:
        ball.reset_position()
        r_score.increment()
        delay = 0.1

screen.exitonclick()
