from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# screen.screensize(canvheight=600, canvwidth=600, bg="black")
screen.title("---The Snake Game---")
screen.tracer(0)


is_game_on = True
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.goup)
screen.onkey(key="Down", fun=snake.godown)
screen.onkey(key="Left", fun=snake.goleft)
screen.onkey(key="Right", fun=snake.goright)

while is_game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.head.distance(food) < 15:
        score.get_point()
        snake.extend()
        food.refresh()
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -299
        or snake.head.ycor() > 299
        or snake.head.ycor() < -280
    ):
        score.game_over()
        is_game_on = False

    for part in snake.body[1:]:
        if snake.head.distance(part) < 5:
            score.game_over()
            is_game_on = False


screen.exitonclick()
