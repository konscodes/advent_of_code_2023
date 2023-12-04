import time
from pathlib import Path

if __name__ == '__main__':
    # Start the timer
    start_time = time.time()

    # Set filepath
    script_path = Path(__file__).resolve()
    file_path = script_path.parent / 'day2.txt'

    test_round = {'red': 12, 'green': 13, 'blue': 14}

    with open(file_path) as f:
        # Split the data into list of strings
        data = f.read().splitlines()
        games = [x.split(sep=': ')[1] for x in data]

        possible_games = []

        for index, game in enumerate(games):
            game_rounds = game.split(sep='; ')
            possible = True
            for game_round in game_rounds:
                pairs = game_round.split(', ')
                for pair in pairs:
                    color = pair.split()[1]
                    value = pair.split()[0]
                    if int(value) > test_round[color]:
                        possible = False
                        break
                
            if possible:
                game_number = index + 1
                possible_games.append(game_number)

    
    print('Part 1:', sum(possible_games))
    print('Part 2:')
    print("--- %s seconds ---" % (time.time() - start_time))
