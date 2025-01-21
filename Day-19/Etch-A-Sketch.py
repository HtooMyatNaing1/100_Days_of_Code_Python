from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.title("Etch-A-Sketch App")

def move_forward():
    turtle.forward(20)

def move_backward():
    turtle.backward(20)

def turning_left():
    turtle.left(10)

def turning_right():
    turtle.right(10)

def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turning_left, key="a")
screen.onkey(fun=turning_right, key="d")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()