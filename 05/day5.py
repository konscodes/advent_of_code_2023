import time
from pathlib import Path

# Start the timer
start_time = time.time()

# Set filepath
script_path = Path(__file__).resolve()
file_path = script_path.parent / 'day5.txt'

# Prepare the data
with open(file_path, 'r') as f:
    data = f.read().split('\n\n')
    data = {x.split(':')[0]: x.split(':')[1].split('\n') for x in data}
    seeds = list(data['seeds'][0].split())
    seed_start = seeds[::2]
    seed_length = seeds[1::2]
    seed_ranges = []
    seed_end = []
    
    for index, seed in enumerate(seed_start):
        seed_range = range(int(seed), int(seed) + int(seed_length[index]))
        seed_ranges.append(seed_range)
        seed_end.append(int(seed) + int(seed_length[index]))

def resolve_map(seed, data) -> list:
    maps = [list(value) for value in data.values()][1:] # all maps excluding seeds
    pathway = [int(seed)]
    for mapping in maps:
        pathway.append(crawl_pathways(mapping, target=pathway[-1]))
    return pathway


def crawl_pathways(mapping, target):
    target = int(target)
    for pathway in mapping:
        if pathway:
            destination, source, span = [int(x) for x in pathway.split()]
            if target in range(source, source + span):
                    new_target = destination - source + target
                    return new_target
    return target


def resolve_backwards(location, data) -> list:
    maps = [list(value) for value in data.values()][1:] # all maps excluding seeds
    pathway = [location]
    for mapping in reversed(maps):
        pathway.append(crawl_backwards(mapping, target=pathway[-1]))
    return pathway


def crawl_backwards(mapping, target):
    target = int(target)
    for pathway in reversed(mapping):
        if pathway:
            destination, source, span = [int(x) for x in pathway.split()]
            if target in range(destination, destination + span):
                    new_target = source - destination + target
                    return new_target
    return target


def find_low():
    locations = list(range(max(seed_end)))

    for location in locations:
        path = resolve_backwards(location, data)
        seed = path[-1]

        for seed_range in seed_ranges:
            if seed in seed_range:
                return path[0]
    
    return None


print('Part 1:', min(resolve_map(seed, data)[-1] for seed in seeds))

# Reversed approach didn't work on input data
#print('Part 2:', find_low())

# Brut approach doesn't work on input data
lows = [min(resolve_map(seed, data)[-1] for seed in batch) for batch in seed_ranges]
print('Part 2:', min(lows))

print("--- %s seconds ---" % (time.time() - start_time))