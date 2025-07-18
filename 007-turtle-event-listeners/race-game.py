from turtle import Turtle, Screen
import random

# tinu = Turtle(shape='turtle')

is_race_on = False
screen = Screen()
screen.setup(height=400, width=500)

user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtules = []

if user_bet:
    is_race_on = True


for i in range(6):
    tinu = Turtle(shape='turtle')
    tinu.color(colors[i])
    tinu.penup()
    tinu.goto(-230, -100 + i * 30)
    # tinu.pendown()
    turtules.append(tinu)

# tinu.penup()
# tinu.goto(-230, 100)

while is_race_on:
    for tinu in turtules:
        tinu.forward(random.randint(0, 10))
        if tinu.xcor() > 210:
            winning_color = tinu.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()