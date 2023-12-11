import time
from pathlib import Path


def win_count(card: list[str]) -> int:
    '''Returns how many winning numbers are there for each card.
    
    Args:
        card (list[str]): Winning numbers on the left and card numbers on the right
    
    Returns:
        int: Number of wins
    '''
    wins = 0
    winning_numbers = card[0].split()
    card_numbers = card[1].split()
    for number in winning_numbers:
        if number in card_numbers:
            wins += 1
    return wins


def card_score(card: list[str]) -> int:
    '''Returns Points calculated for each card.

    Args:
        card (list[str]): Winning numbers on the left and card numbers on the right

    Returns:
        int: Points for a card
    '''
    points = 0
    winning_numbers = card[0].split()
    card_numbers = card[1].split()
    for number in winning_numbers:
        if number in card_numbers:
            if points == 0:
                points += 1
            else:
                points = points * 2
    return points


# Start the timer
start_time = time.time()

# Set filepath
script_path = Path(__file__).resolve()
file_path = script_path.parent / 'day4.txt'

# Prepare the data
with open(file_path, 'r') as f:
    data = f.read().splitlines()
    cards_data = [x.split(sep=': ')[1] for x in data]
    card_names = [x.split(sep=': ')[0] for x in data]
    cards = [x.split(sep=' | ') for x in cards_data]

print('Part 1:', sum(card_score(card) for card in cards))

cards_count = {name: 1 for name in card_names}
for index, card in enumerate(cards):
    wins = win_count(card)
    for next_index in range(1, wins + 1):
        cards_count[card_names[index +
                               next_index]] += cards_count[card_names[index]]

print('Part 2:', sum(cards_count.values()))
print("--- %s seconds ---" % (time.time() - start_time))
