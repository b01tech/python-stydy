from turtle import Screen
from player import Player
from score_board import ScoreBoard
from car import Car
import time

screen = Screen()

screen.tracer(0)
player = Player()
score_bd = ScoreBoard()

cars = []

for _ in range(score_bd.difficulty):
    car = Car()
    cars.append(car)

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 280:
        player.reset()
        score_bd.get_score()
        for _ in range(score_bd.difficulty):
            car = Car()
            cars.append(car)

    screen.listen()
    screen.onkey(fun=player.move, key="Up")

    for i in range(len(cars)):
        if player.distance(cars[i]) < 20:
            is_game_on = False
        cars[i].move()
        if cars[i].xcor() < -350:
            cars[i].reset()

score_bd.game_over()

screen.exitonclick()
