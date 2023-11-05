from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race . Enter your color :")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
def_x = -240
def_y = -110
turtles = []
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(def_x, def_y)
    def_y += 30
    turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"well done . you've won. the {wining_color} turtle is a wining turtle")
            else:
                print(f"you've lost. the {wining_color} turtle was the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()
