import random
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cpu_cards = []
player_cards = []


def pick_card():
    card_pos = random.randint(0, 12)
    # print(card_pos)
    return CARDS[card_pos]


def cpu_pick():
    cpu_card = pick_card()
    return cpu_cards.append(cpu_card)


def player_pick():
    player_card = pick_card()
    return player_cards.append(player_card)


def show_hands():
    print(f"CPU hand: {cpu_cards}")
    print(f"Player hand: {player_cards}")


def check_winner():
    player_score = sum(player_cards)
    if player_score > 21:
        print("You lose!!!")
        return False
    elif player_score == 21:
        print("You win!!!")
        return False
    else:
        return True


def get_card():
    answer = input("Do you want pick a card? y or n:")
    if answer == 'y':
        player_pick()
    elif answer == 'n':
        check_winner()
    else:
        print("Invalid input.")
        get_card()


def play():
    keep_playing = check_winner()
    while keep_playing:
        get_card()
        show_hands()
        keep_playing = check_winner()


def start():
    print('Welcome to blackjack game!')
    cpu_pick()
    player_pick()
    player_pick()
    show_hands()
    play()


start()
