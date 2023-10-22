import turtle

import colorgram
from turtle import Turtle, Screen
import random

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61),
              (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39),
              (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202),
              (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205),
              (223, 178, 169)]

tim = Turtle()
tim.hideturtle()
tim.penup()
height = 10
turtle.colormode(255)
tim.speed("fastest")
tim.shape("arrow")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


while height > 0:
    for _ in range(10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50, )
        tim.dot(20, random.choice(color_list))
    tim.backward(500)
    tim.setheading(90)
    tim.forward(50)
    tim.right(90)
    height -= 1

screen = Screen()
screen.exitonclick()
