import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from lineturtle import LineDraw

game_is_on = True
positions = {"left":(-30, 250), "right":(30, 250)}
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

drawer = LineDraw()
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
left_score_writer = Scoreboard(positions["left"])
right_score_writer = Scoreboard(positions["right"])

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320\
        or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380: # right
        ball.reset_position()
        # left score writer here
        left_score_writer.increase_score()
    elif ball.xcor() < -380: # left
        ball.reset_position()
        # right score writer here
        right_score_writer.increase_score()

screen.exitonclick()