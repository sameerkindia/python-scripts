from turtle import Screen, Turtle


tinu = Turtle()

def move_forward():
    tinu.forward(10)

def move_backward():
    tinu.backward(10)

def turn_left():
    tinu.left(10)

def turn_right():
    tinu.right(10)

def clear_screen():
    tinu.clear()
    tinu.penup()
    tinu.home()
    tinu.pendown()


screen = Screen()
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_screen, "c")

screen.exitonclick()