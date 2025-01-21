# import colorgram

# colors = colorgram.extract("Spot_painting.jpg", 30)
#
# color_tuples = []
#
# for i in range(len(colors)):
#     color = colors[i]
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuples.append((r,g,b))
#
# print(color_tuples)
###################################################################################################

import turtle as t
import random

x_cor = 250.00
y_cor = 200.00
turtle = t.Turtle()
t.colormode(255)
turtle.teleport(-x_cor, -y_cor)
turtle.shape("turtle")
turtle.shapesize(0.5)
turtle.speed("fastest")

random_colors_extracted = [(198, 91, 65), (40, 81, 11), (91, 21, 26), (133, 173, 108),
                           (113, 162, 82), (138, 167, 176), (211, 203, 147), (46, 79, 9),
                           (178, 152, 156), (19, 81, 97), (176, 204, 180), (222, 178, 170),
                           (153, 114, 119), (97, 138, 148), (104, 43, 31), (22, 64, 45),
                           (62, 133, 113), (105, 39, 45), (184, 149, 98), (150, 102, 46),
                           (83, 31, 23), (179, 150, 25), (11, 56, 72), (34, 100, 120),]

number_of_dots = 10

for row in range(number_of_dots):
    for column in range(number_of_dots):
        turtle.dot(25, random.choice(random_colors_extracted))
        turtle.penup() # Comment this line to make delicious and colorful meatballs :)
        turtle.forward(50)
    turtle.teleport(-x_cor, turtle.ycor()+50)

screen = t.Screen()
screen.exitonclick()
