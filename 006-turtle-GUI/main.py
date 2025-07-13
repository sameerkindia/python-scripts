from turtle import Turtle,Screen
import random

tinu = Turtle()
# Square
# tinu.shape("turtle")
# tinu.color('green')
# tinu.forward(100)
# tinu.left(90)
# tinu.forward(100)
# tinu.left(90)
# tinu.forward(100)
# tinu.left(90)
# tinu.forward(100)


# Draw a dashed line
# def draw_dashed_line(length, dash_length=10, gap_length=5):
#     # for _ in range(length // (dash_length + gap_length)):
#     for _ in range(length):
#         tinu.forward(dash_length)   # draw dash
#         tinu.penup()
#         tinu.forward(gap_length)    # skip gap
#         tinu.pendown()

# # Call the function
# draw_dashed_line(15,10,5)



# tinu.speed(2)

def draw_shape(sides):
    for i in range(sides):
        deg = 3 + i
        # Set random color based on the iteration
        tinu.color((random.random(), random.random(), random.random()))
        # tinu.color((round(i / 4), 0.5, 1))  # Change color based on iteration
        for _ in range(deg):
            tinu.forward(100)
            tinu.right(360 / deg)

draw_shape(10)



screen = Screen()
screen.exitonclick()