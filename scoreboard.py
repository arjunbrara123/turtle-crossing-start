from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 230)
        self.level = 0
        self.refresh()

    def refresh(self, level=0):
        self.clear()
        self.level = level
        self.write(f"Level: {level}", move=False, align="left", font=FONT)

    def game_over(self, level):
        """Game over on screen"""
        self.clear()
        self.write(f"GAME OVER! Level: {level}", align="left", font=FONT)  # Write 'Game Over' message
