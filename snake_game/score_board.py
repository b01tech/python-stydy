from turtle import Turtle

FONT = ("Arial", 10, "bold")
ALIGN = 'center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.ht()
        self.goto(-20, 280)
        self.color("white")
        self.write(arg=f'Score: {self.points}', font=FONT)
        self.get_point

    def get_point(self):
        self.points += 1
        self.clear()
        self.write(arg=f'Score: {self.points}', font=("Arial", 10, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
