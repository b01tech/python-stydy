import random


def set_difficulty(difficulty):
    if difficulty == 'easy':
        return 10
    else:
        return 5


def check_num(guess, attempts, num):
    if guess == num:
        print(f"You win! The number is {num}.")
        attempts = 0
        return attempts
    elif guess < num:
        print("Too low.")
        print("Guess again")
        attempts -= 1
        return attempts
    elif guess > num:
        print("Too high.")
        print("Guess again")
        attempts -= 1
        return attempts


def make_guess(attempts, num):
    guess = int(input("Make a guess: "))
    return check_num(guess, attempts, num)


def play(attempts, num):
    while attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        attempts = make_guess(attempts, num)
    gameOver()


def gameOver():
    print("Game Over!!!")
    return


def set_num():
    num = random.randint(1, 100)
    return num


print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
num = set_num()
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = set_difficulty(difficulty)
play(attempts, num)
