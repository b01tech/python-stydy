from score_board import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

is_game_on = True

score_board = ScoreBoard()
pad1 = Paddle(1)
pad2 = Paddle(2)
ball = Ball()

score_board.screen.onkey(fun=pad1.go_up, key="Up")
score_board.screen.onkey(fun=pad1.go_down, key="Down")
score_board.screen.onkey(fun=pad2.go_up, key="w")
score_board.screen.onkey(fun=pad2.go_down, key="s")

while is_game_on:
    time.sleep(ball.move_speed)
    score_board.screen.listen()
    ball.move()
    if (
        ball.distance(pad1) < 50
        and ball.xcor() > 320
        or ball.distance(pad2) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()
    if ball.xcor() > 400:
        score_board.score(1)
        ball.reset()
    elif ball.xcor() < -400:
        score_board.score(2)
        ball.reset()

score_board.screen.exitonclick()
