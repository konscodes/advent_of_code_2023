import time
from pathlib import Path


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
    cards = [x.split(sep=': ')[1] for x in data]
    cards = [x.split(sep=' | ') for x in cards]

print('Part 1:', sum(card_score(card) for card in cards))

print("--- %s seconds ---" % (time.time() - start_time))