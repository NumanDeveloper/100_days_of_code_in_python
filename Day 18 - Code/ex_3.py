from turtle import Turtle, Screen
from random import choice
t = Turtle()

colors = ['red', 'green', 'yellow', 'purple', 'pink']


def draw_shape(sides):
    # first calculate at which to move turtle
    angle = 360 / sides
    for i in range(sides):
        t.forward(100)
        t.right(angle)


for sides in range(3, 10):
    t.color(choice(colors))
    draw_shape(sides)
s = Screen()
s.exitonclick()
