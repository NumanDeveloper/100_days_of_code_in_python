from turtle import Screen, Turtle

t = Turtle()

for i in range(10):
    t.forward(5)
    t.penup()  # pens up the pen mean stop drawing
    t.forward(5)
    t.pendown()  # pens down the pen mean start drawing


screen = Screen()
screen.exitonclick()
