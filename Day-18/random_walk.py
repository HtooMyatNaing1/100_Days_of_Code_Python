import turtle as t
from random import choice,randint

turtle = t.Turtle()
t.colormode(255)
turtle.shape("turtle")
turtle.shapesize(0.5)
turtle.pensize(15)
turtle.speed("fastest")

directions = ["right", "left", "fw", "bw"]

def random_color():
    r = randint(0, 255) # red
    g = randint(0, 255) # green
    b = randint(0, 255) # blue
    resultant_color = (r, g, b)
    return resultant_color

def random_move():
    direction = choice(directions)
    match direction:
        case "right":
            turtle.right(90)
            turtle.forward(30)
        case "left":
            turtle.left(90)
            turtle.forward(30)
        case "fw":
            turtle.forward(30)
        case "bw":
            turtle.backward(30)

for move in range(500):
    turtle.color(random_color())
    random_move()

screen = t.Screen()
screen.exitonclick()