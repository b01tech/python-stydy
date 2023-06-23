from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.move()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_part(position)

    def add_part(self, position):
        snake_part = Turtle(shape='square')
        snake_part.pu()
        snake_part.color('white')
        snake_part.goto(position)
        self.body.append(snake_part)

    def extend(self):
        self.add_part(self.body[-1].position())

    def move(self):
        for part in range(len(self.body)-1, 0, -1):
            new_x = self.body[part - 1].xcor()
            new_y = self.body[part - 1].ycor()
            self.body[part].goto(new_x, new_y)
        self.head.forward(SPEED)

    def goup(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def godown(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def goleft(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def goright(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
