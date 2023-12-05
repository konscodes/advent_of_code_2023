import time
from pathlib import Path


def valid_neighbor(neighbor: tuple):
    grid_range = range(len(data))
    x,y = neighbor
    in_range = bool(x in grid_range and y in grid_range)
    already_marked = bool(schematic_map[x][y] == 1) if in_range else True
    return in_range and not already_marked


def crawl_neighbors(position: tuple):
    '''
    Check the neighbors of position. 
    If numbers update schematic_map and check the neighbors again
    '''
    i,j = position
    neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1),
                (i, j-1), (i, j+1),
                (i+1, j+1), (i+1, j), (i+1, j-1)]
    for neighbor in neighbors:
        if valid_neighbor(neighbor):
            x,y = neighbor
            if schematic[x][y] in numbers:
                schematic_map[x][y] = 1
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
for i, line in enumerate(data):
    for j, value in enumerate(line):
        if value not in numbers + '.':
            position = (i, j)
            crawl_neighbors(position)

# At this point the schematic map is filled with valid markers
# Extract corresponding part numbers from schematic
part_numbers = []
number = ''
for i in range(len(schematic_map)):
    for j in range(len(schematic_map)):
        if schematic_map[i][j] == 1:
            number += schematic[i][j]
        else:
            part_numbers.append(int(number)) if number else None
            number = ''


print('Part 1:', sum(part_numbers))
print('Part 2:')

print("--- %s seconds ---" % (time.time() - start_time))
