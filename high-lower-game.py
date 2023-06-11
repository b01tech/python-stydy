import random

POPULATION = {
    'Brazil': 212559417,
    'China': 1439323776,
    'Argentina': 45195774,
    'USA': 331002351,
    "Mexico": 128932753,
    'Canada': 37742154,
    "Japan": 126476461,
    "India": 1380004385,
    "Russia": 145934462,
    "New Zealand": 4822233,
    "Greece": 10423054,
    "Iran": 83992949,
    "Spain": 46754778
}

is_gameover = False

score = 0
while not is_gameover:
    answer = ''
    key_A, value_A = random.choice(list(POPULATION.items()))
    key_B, value_B = random.choice(list(POPULATION.items()))
    while value_A == value_B:
        key_B, value_B = random.choice(list(POPULATION.items()))
    if value_A > value_B:
        answer = 'y'
    else:
        answer = 'n'
    guess = input(
        f"{key_A} has a higher population than {key_B}? Type 'y' or 'n': ")
    if guess == answer:
        print("Right!")
        print(f"{key_A} has {value_A} and {key_B} has {value_B}")
        score += 1
        print(f"Your score is {score}")
    else:
        print("WRONG!")
        print(f"{key_A} has {value_A} and {key_B} has {value_B}")
        is_gameover = True
        print(f"Your Final score is {score}")

# play_game()
