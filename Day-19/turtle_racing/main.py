from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.title("Turtle Racing Game")
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter color: ")

colors = ["red", "purple", "blue", "yellow", "green", "black"]
turtles = []
y_position = -70
y_start_positions = []
for i in range(len(colors)):
    y_start_positions.append(y_position)
    y_position += 30

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto((-225, y_start_positions[turtle_index]))
    turtles.append(new_turtle)

def writing_turtle():
    drawturtle = Turtle()
    drawturtle.hideturtle()
    drawturtle.penup()
    drawturtle.goto(-160, 0)
    return drawturtle

if user_bet:
    is_race_on = True

drawer_turtle = writing_turtle()

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                drawer_turtle.write(f"You've won. The {winning_color} turtle has won.", align="left", font=("Arial", 14, "normal"))
            else:
                drawer_turtle.write(f"You've lost. The {winning_color} turtle has won.", align="left", font=("Arial", 14, "normal"))

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
