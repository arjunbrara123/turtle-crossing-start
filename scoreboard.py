from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0

    def refresh(self, score=0):
        self.clear()
        self.score = score
        self.write(f"Level: {score}", move=False, align="center", font=FONT)
