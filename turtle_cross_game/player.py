from turtle import Turtle

COLOR = "green"


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.shape("turtle")
        self.pu()
        self.left(90)
        self.reset()

    def reset(self):
        self.goto(0, -250)

    def move(self):
        self.forward(30)
