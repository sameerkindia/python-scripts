from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
# class Scoreboard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.high_score = 0
#         self.load_high_score()
#         self.color("white")
#         self.penup()
#         self.hideturtle()
#         self.goto(0, 260)
#         self.update_scoreboard()

#     def load_high_score(self):
#         try:
#             with open("high_score.txt", "r") as file:
#                 self.high_score = int(file.read())
#         except FileNotFoundError:
#             self.high_score = 0

#     def save_high_score(self):
#         with open("high_score.txt", "w") as file:
#             file.write(str(self.high_score))

#     def update_scoreboard(self):
#         self.clear()
#         self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

#     def increase_score(self):
#         self.score += 1
#         if self.score > self.high_score:
#             self.high_score = self.score
#             self.save_high_score()
#         self.update_scoreboard()
    