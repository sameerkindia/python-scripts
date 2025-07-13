from turtle import Turtle, Screen, colormode
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


# *****Draw Shapes

# tinu.speed(2)

# def draw_shape(sides):
#     for i in range(sides):
#         deg = 3 + i
#         # Set random color based on the iteration
#         tinu.color((random.random(), random.random(), random.random()))
#         # tinu.color((round(i / 4), 0.5, 1))  # Change color based on iteration
#         for _ in range(deg):
#             tinu.forward(100)
#             tinu.right(360 / deg)

# draw_shape(10)

# Random Walk

colormode(255)  # Enable RGB color mode

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb = (r, g, b)
    return random_rgb


def random_walk():
    tinu.speed("fastest")
    tinu.pensize(5)

    colors = ["red", "blue", "green", "orange", "purple", "yellow", "black"]

    directions = [0, 90, 180, 270]

    for _ in range(200):
        # tinu.color(random.choice(colors))
        tinu.color(random_color())
        tinu.forward(30)
        tinu.setheading(random.choice(directions))

random_walk()


screen = Screen()
screen.exitonclick()
