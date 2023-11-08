from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()

screen.setup(height= 600 , width= 800)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
first_paddle = Paddle((350,0))
second_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(first_paddle.up, "Up")
screen.onkey(first_paddle.down, "Down")
screen.onkey(second_paddle.up, "w")
screen.onkey(second_paddle.down, "s")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.moving_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(first_paddle) < 50 and ball.xcor() > 320 or ball.distance(second_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

screen.exitonclick()