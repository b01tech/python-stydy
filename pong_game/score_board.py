from turtle import Turtle, Screen

WIDTH = 800
HEIGHT = 600
COLOR = "white"
BGCOLOR = "black"
FONT = ("Arial", 30, "bold")
ALIGN = "center"


class ScoreBoard:
    def __init__(self):
        self.score_board = Turtle()
        self.score_board.ht()
        self.score_board.pu()
        self.score_board.color(COLOR)
        self.sc_player_1 = 0
        self.sc_player_2 = 0
        self.show()
        self.update_score()

    def show(self):
        self.screen = Screen()
        self.screen.title("PONG GAME")
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.bgcolor(BGCOLOR)

    def update_score(self):
        self.score_board.goto(0, 250)
        self.score_board.clear()
        self.score_board.write(
            arg=f"{self.sc_player_1}\t{self.sc_player_2}", align=ALIGN, font=FONT
        )

    def score(self, player):
        if player == 1:
            self.sc_player_1 += 1
        elif player == 2:
            self.sc_player_2 += 1
        self.update_score()
