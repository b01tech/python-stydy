from turtle import Turtle
from score_board import COLOR

MOVE_X = 10
MOVE_Y = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(COLOR)
        self.left(45)
        self.pu()
        self.xmove = MOVE_X
        self.ymove = MOVE_Y
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
        self.bounce_y()

    def bounce_y(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.5

    def reset(self):
        self.ht()
        self.goto(0, 0)
        self.st()
        self.move_speed = 0.05
        self.bounce_x()
