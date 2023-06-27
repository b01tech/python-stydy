import turtle
import pandas as pd


screen = turtle.Screen()
screen.setup(width=600, height=600)
MAP_BR = "./brazil_map.gif"

screen.addshape(MAP_BR)
turtle.shape(MAP_BR)

data = pd.read_csv("./brazil_states.csv")
# print(data.states)

score = 0

while score < 27:
    user_answer = turtle.textinput(
        title=f"Score: {score}/27", prompt="Type a State of Brazil:").title()
    list_states = list(data.states)
    if user_answer in list_states:
        state = data.loc[data.states == user_answer]
        text = turtle.Turtle()
        text.pu()
        text.ht()
        text.goto(int(state.x), int(state.y))
        text.write(user_answer)
        score += 1
    else:
        print(user_answer)
