from turtle import Turtle
from score_board import COLOR

PLAYER1_POS = (350, 0)
PLAYER2_POS = (-350, 0)


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.color(COLOR)
        self.speed("fastest")
        if player == 1:
            self.goto(PLAYER1_POS)
            self.st()
        elif player == 2:
            self.goto(PLAYER2_POS)
            self.st()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
