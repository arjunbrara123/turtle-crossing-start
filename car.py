from turtle import Turtle


class Car(Turtle):

    def __init__(self, col, ypos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(col)
        self.penup()
        self.setheading(180)
        self.setpos(280, ypos)

