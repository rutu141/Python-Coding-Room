import turtle
from turtle import Turtle,Screen
turtle = Turtle()
turtle.shape("turtle")
turtle.color("medium purple")

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

for i in range(0,5):
    print(i)
    turtle.color("medium purple")
    turtle.forward(10)
    turtle.color("white")
    turtle.forward(10)



screen=Screen()
screen.exitonclick()
