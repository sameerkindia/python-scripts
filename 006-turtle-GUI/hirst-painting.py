# import colorgram

# rgb_colors = []
# colors = colorgram.extract('painting.jpg', 20)

# # print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random

selected_colors = [(235, 234, 232), (237, 238, 240), (243, 235, 240), (230, 241, 236), (166, 96, 23), (227, 137, 74), (15, 32, 55), (237, 78, 95), (45, 106, 147), (222, 212, 3),
                   (144, 178, 207), (211, 150, 161), (132, 216, 206), (239, 94, 37), (164, 45, 135), (84, 181, 7), (52, 91, 85), (135, 216, 221), (231, 210, 83), (202, 140, 17)]

tinu = Turtle()
colormode(255)  # Enable RGB color mode

def draw_dots():
    tinu.penup()
    tinu.hideturtle()
    tinu.speed("fastest")
    tinu.setheading(225)
    tinu.forward(300)
    tinu.setheading(0)

    for _ in range(10):
        for _ in range(10):
            tinu.dot(20, random.choice(selected_colors))
            tinu.forward(50)
        tinu.setheading(90)
        tinu.forward(50)
        tinu.setheading(180)
        tinu.forward(500)
        tinu.setheading(0)

    

draw_dots()

screen = Screen()
screen.exitonclick()