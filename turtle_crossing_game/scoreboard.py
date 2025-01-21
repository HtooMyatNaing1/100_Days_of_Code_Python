from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_LOCATION = (-260, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_LOCATION)
        self.score_writer()

    def score_writer(self):
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def score_increase(self):
        self.level += 1
        self.clear()
        self.score_writer()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="Center", font=FONT)
