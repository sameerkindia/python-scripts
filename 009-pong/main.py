from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

# paddle = Turtle('square')
# paddle.color('white')
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350, 0)

# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor() , new_y)

# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor() , new_y)


paddle_l = Paddle((-350 , 0))
paddle_r = Paddle((350 , 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.go_up , 'Up')
screen.onkey(paddle_r.go_down , 'Down')
screen.onkey(paddle_l.go_up , 'w')
screen.onkey(paddle_l.go_down , 's')




is_game_on = True

while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Left 
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_l_score()
    
    # Right
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_r_score()




screen.exitonclick()