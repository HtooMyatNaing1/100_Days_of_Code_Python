from turtle import Turtle

class LineDraw(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.drawline()

    def drawline(self):
        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.forward(400)
        self.right(90)
        self.forward(600)
        self.right(90)
        self.forward(800)
        self.right(90)
        self.forward(600)
        self.right(90)
        self.forward(400)
