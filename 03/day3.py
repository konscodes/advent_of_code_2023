import time
from pathlib import Path


def valid_neighbor(neighbor: tuple):
    grid_range = range(len(data))
    x, y = neighbor
    in_range = bool(x in grid_range and y in grid_range)
    already_marked = bool(schematic_map[x][y]) if in_range else True
    return in_range and not already_marked


def crawl_neighbors(starting_coordinates: tuple):
    '''
    Check the neighbors of position. 
    If numbers update schematic_map and check the neighbors again
    '''
    i, j = starting_coordinates
    neighbors = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
                 (i, j + 1), (i + 1, j + 1), (i + 1, j), (i + 1, j - 1)]
    for neighbor in neighbors:
        if valid_neighbor(neighbor):
            x, y = neighbor
            if schematic[x][y] in numbers:
                schematic_map[x][y] = position
                crawl_neighbors(neighbor)


# Start the timer
start_time = time.time()

# Set filepath
script_path = Path(__file__).resolve()
file_path = script_path.parent / 'day3.txt'

with open(file_path) as f:
    # Split the data into list of strings
    data = f.read().splitlines()

# Schematic with all symbols in it in a grid
schematic = [list(line) for line in data]

# Schematic map that will be populated with number locations that we need to sum up
schematic_map = [[0 for _ in range(len(data))] for _ in range(len(data))]

# Take symbol position (i,j) and start crawling neighbors
numbers = '01234567890'
gears = []
for i, line in enumerate(data):
    for j, value in enumerate(line):
        if value not in numbers + '.':
            position = (i, j)
            if value == '*':
                gears.append(position)
            crawl_neighbors(position)
'''At this point the schematic map is filled with valid markers, 
each one representing coordinates of its adjacent symbol.
We will extract corresponding part numbers from schematic and 
populate the dict matching each symbol to its numbers.'''
part_numbers = {}
number = ''
tuple_value = ()
for i in range(len(schematic_map)):
    for j in range(len(schematic_map)):
        if schematic_map[i][j]:
            tuple_value = schematic_map[i][j]
            number += schematic[i][j]
        else:
            part_numbers.setdefault(tuple_value, []).append(
                int(number)) if number else None
            number = ''

print('Part 1:', sum(sum(numbers) for numbers in part_numbers.values()))
'''At this point we have a dict matching symbols to all of their adjacent numbers.
We just need to take and multiply only those that match Part 2 criteria for a gear.'''
multiplication_sum = 0
for key in gears:
    if key in part_numbers and len(part_numbers[key]) == 2:
        multiplication_result = part_numbers[key][0] * part_numbers[key][1]
        multiplication_sum += multiplication_result

print('Part 2:', multiplication_sum)

print("--- %s seconds ---" % (time.time() - start_time))
