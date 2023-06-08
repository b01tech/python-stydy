bids = {}
bidding_finhed = False


def chose_winner():
    winner_value = 0
    winner = ''
    for bidder in bids:
        if bids[bidder] > winner_value:
            winner_value = bids[bidder]
            winner = bidder
    print(f"The winner is {winner} with $ {winner_value}")


while not bidding_finhed:
    name = input('What is your name?: ')
    value = input('What is your bid? $')
    bids[name] = int(value)
    should_continue = input('Are there any other bidders? Type yes or no: ')
    if should_continue == 'no':
        bidding_finhed = True
chose_winner()
