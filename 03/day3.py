import time
from pathlib import Path


def neighbours(position: tuple):
    # Check the neighbours of position
    # If numbers update schematic_map and check the neighbours again
    i,j = position
    return i,j


# Start the timer
start_time = time.time()

# Set filepath
script_path = Path(__file__).resolve()
file_path = script_path.parent / 'test.txt'

with open(file_path) as f:
    # Split the data into list of strings
    data = f.read().splitlines()

filters = '01234567890.'


    
# Schematic with all symbols in it in a grid
schematic = [[x for x in line] for line in data]

# Schematic map that will be populated with number locations that we need to sum up
schematic_map = [[0] * len(data)] * len(data)

# Schematic map with only special symbol location (i,j)
symbol_map = [[(i, j) if value not in filters else 0
               for j, value in enumerate(line)] for i, line in enumerate(data)]

for i, line in enumerate(data):
    for j, value in enumerate(line):
        position = (i, j) if value not in filters
        test = neighbours(position)

print('Part 1:')
print('Part 2:')

print("--- %s seconds ---" % (time.time() - start_time))
