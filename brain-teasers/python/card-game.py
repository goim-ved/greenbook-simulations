import random

def playGame():
    deck = ['R'] * 26 + ['B'] * 26
    random.shuffle(deck)

    your_pile = 0
    dealer_pile = 0

    for i in range(0, 52, 2):
        c1 = deck[i]
        c2 = deck[i+1]

        if c1 == 'R' and c2 == 'R':
            your_pile += 2
        elif c1 == 'B' and c2 == 'B':
            dealer_pile += 2

    return  your_pile, dealer_pile

wins = 0
loss = 0
ties = 0

for i in range(10000):
    you, dealer = playGame()
    if you > dealer:
        wins += 1
    elif you < dealer:
        loss += 1
    else:
        ties += 1

print(f"Wins: {wins}")
print(f"Losses: {loss}")
print(f"Ties: {ties}")