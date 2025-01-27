import turtle
from tkinter.constants import CENTER

import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

guessed_states = []
csv_file = pd.read_csv("50_states.csv")
all_states = csv_file.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = csv_file[csv_file.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        guessed_states.append(answer_state)

    if len(guessed_states) == 50:
        drawer = turtle.Turtle()
        drawer.hideturtle()
        drawer.color("red")
        drawer.penup()
        drawer.goto(0, 0)
        drawer.write("Congratulations! You are a genius.", align=CENTER, font=("Arial", 24, "normal"))
        break

screen.exitonclick()