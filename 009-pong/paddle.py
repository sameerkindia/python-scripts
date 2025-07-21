# from turtle import Turtle

# class Paddle:
#     def __init__(self, cor):
#         self.paddle = Turtle('square')
#         self.paddle.color('white')
#         self.paddle.shapesize(stretch_wid=5, stretch_len=1)
#         self.paddle.penup()
#         self.paddle.goto(cor)

#     def go_up(self):
#         new_y = self.paddle.ycor() + 20
#         self.paddle.goto(self.paddle.xcor() , new_y)

#     def go_down(self):
#         new_y = self.paddle.ycor() - 20
#         self.paddle.goto(self.paddle.xcor() , new_y)



from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(cor)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor() , new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor() , new_y)