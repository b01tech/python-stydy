import turtle as t
import colorgram as cg
import random

t.colormode(255)
colors = cg.extract('./hirst_picture.jpg', 12)


timmy = t.Turtle()
timmy.ht()
timmy.pu()
timmy.speed('fastest')


def start(size):
    origin = -150 - size * 10
    timmy.setpos(origin, origin)
    draw_pic(size, origin)


def set_color():
    i = random.randint(0, 11)
    color = colors[i].rgb
    return color


def draw_line(size):
    for _ in range(size):
        new_color = set_color()
        timmy.dot(20, new_color)
        timmy.forward(50)


def new_line(origin):
    new_posy = timmy.ycor() + 50
    timmy.sety(new_posy)
    timmy.setx(origin)


def draw_pic(size, origin):
    for _ in range(size):
        draw_line(size)
        new_line(origin)


start(12)
screen = t.Screen()
screen.exitonclick()
