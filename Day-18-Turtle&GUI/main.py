import random
import turtle
from turtle import Turtle, Screen

# import turtle
# from turtle import *
# import turtle as t

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# # square
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pu()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pd()
#

'''
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for shape_side_n in range(3,11):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)

'''

t = Turtle()
t.pensize(5)
t.speed("fastest")
turtle.colormode(255)
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black"]

directions = [0, 90, 180, 270]

for _ in range(200):
    t.color(random.choice(colors))
    t.forward(30)
    t.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

# tuples are immutable
