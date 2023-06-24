from turtle import Turtle
import random

COLORS = ["red", "blue", "yellow", "purple", "gray"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("square")
        self.shapesize(stretch_len=random.randint(1, 2), stretch_wid=1)
        self.reset()

    def move(self):
        new_x = self.xcor() - self.move_speed
        self.goto(new_x, self.ycor())

    def reset(self):
        self.color(random.choice(COLORS))
        start_x = random.randint(300, 400)
        start_y = random.randint(-200, 250)
        self.goto(start_x, start_y)
        self.move_speed = (random.randint(5, 60))
