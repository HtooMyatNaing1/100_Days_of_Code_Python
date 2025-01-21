import turtle as t
from random import randint

turtle = t.Turtle()
t.colormode(255)
turtle.speed("fastest")

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r,g,b

def draw_spirograph(changed_degree):
    for i in range(int(360/changed_degree)):
        turtle.circle(100)
        turtle.setheading(turtle.heading()+changed_degree)
        turtle.color(random_color())

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()