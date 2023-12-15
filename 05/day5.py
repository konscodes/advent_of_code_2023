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
    
    for index, seed in enumerate(seed_start):
        seed_range = range(int(seed), int(seed) + int(seed_length[index]))
        seed_ranges.append(seed_range)

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


print('Part 1:', min(resolve_map(seed, data)[-1] for seed in seeds))

lows = [min(resolve_map(seed, data)[-1] for seed in batch) for batch in seed_ranges]
print('Part 2:', min(lows))

print("--- %s seconds ---" % (time.time() - start_time))