import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

think_num = random.randint(1, 100)


def difficulty():
    dif = ''
    while dif != 'easy' or dif != 'hard':
        dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if dif == 'easy':
            attempts = 10
            return attempts
        elif dif == 'hard':
            attempts = 5
            return attempts
        else:
            print("Input invalid.")


tries = difficulty()
is_gameover = False


def guess_wrong():
    global tries
    global is_gameover
    tries -= 1
    if tries > 0:
        print(f"You have {tries} attempts remaining.")
    else:
        print("You have NO attempts. Game is over!")
        is_gameover = True


def guess_number():
    global is_gameover
    while not is_gameover:
        num = int(input("Make a guess: "))
        if num == think_num:
            print("You win!")
            is_gameover = True
        elif num < think_num:
            print("Too low! Guess again.")
            guess_wrong()
        elif num > think_num:
            print("Too high! Guess again.")
            guess_wrong()


guess_number()
