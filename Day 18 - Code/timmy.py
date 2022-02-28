from turtle import Turtle, Screen
# Note: Don't name your file 'turtle.py', it will raise error
# creating timmy object from Turtle class
timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')
timmy.left(90)
timmy.forward(100)
timmy.right(135)
timmy.forward(100)
timmy.left(135)
timmy.forward(100)

# put the screen related code at the end since it helps lock screen
my_screen = Screen()
my_screen.exitonclick()
