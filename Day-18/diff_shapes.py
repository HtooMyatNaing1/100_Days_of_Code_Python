import turtle as t
from random import randint

my_turtle = t.Turtle()
t.colormode(255)
my_turtle.shape("turtle")
my_turtle.pensize(10)
my_turtle.speed("fastest")

def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    resultant_color = (red, green, blue)
    return resultant_color

def draw(sides):
    degree = 360/sides
    for i in range(sides):
        my_turtle.forward(100)
        my_turtle.right(degree)

n_of_sides = 3
while n_of_sides <= 10:
    my_turtle.color(random_color())
    draw(n_of_sides)
    n_of_sides += 1

# For windows
my_screen = t.Screen()
my_screen.exitonclick()