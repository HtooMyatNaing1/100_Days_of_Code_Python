from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def high_score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
