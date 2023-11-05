from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

game_is_on = True
snake = Snake()
food = Food()
screen = Screen()
scoreboard = ScoreBoard()
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
