from pathlib import Path
from unittest import skip

def is_valid_position(data, i, j):
    return i >= 0 and i < len(data) and \
           j >= 0 and j < len(data[0])


def neighbors(data, i, j):
    return [(i+x, j+y) for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1), 
                                    (-1, 1), (-1, -1), (1, -1), (1, 1)]
                        if is_valid_position(data, i+x, j+y)]


def outbreak(flashes, nearby):
    for a,b in nearby:
        if data[a][b] == 9:
            data[a][b] = 0
            flashes.append((a,b))
            outbreak(flashes, neighbors(data, a,b))
        elif data[a][b] == 0 and (a,b) in flashes:
            pass
        else: data[a][b] += 1
    return 0


def energy_levels(data):
    flashes = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 9:
                data[i][j] = 0
                flashes.append((i,j))
                outbreak(flashes, neighbors(data, i,j))
            elif data[i][j] == 0 and (i,j) in flashes:
                pass
            else: data[i][j] += 1
    return len(flashes)


def count_flashes(data):
    total = 0
    for i in range(1000):
        if i == 100:
            print('part1:', total)
        iteration = energy_levels(data)
        if iteration == 100:
            print('part2:', i+1)
            return total
        else: total += iteration
        

if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'day11.txt'

    with open(file) as f:
        data = f.read().splitlines()
        data = [[int(y) for y in x] for x in data]
    
    count_flashes(data)