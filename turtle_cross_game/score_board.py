from turtle import Turtle

ALIGN = "left"
FONT = ("arial", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.score = 0
        self.difficulty = 1
        self.pu()
        self.goto(-320, 270)
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def get_score(self):
        self.score += 1
        self.difficulty += self.score
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(-50, 0)
        self.write(arg=f"GAME OVER", align=ALIGN, font=FONT)
