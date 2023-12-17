# [Day 5: If You Give A Seed A Fertilizer](https://adventofcode.com/2023/day/5)

## Part 1: Find the lowest location number that corresponds to any of the initial seeds
The logic sounds very complicated at first but the implementation is not that hard. 
In the end we need to get a chain of connected dots:

'''
Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
...
'''

This looks like a list for each seed [79, ] that we need to append with newly discovered paths. 

'''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48
'''

Looking at the first map and taking our initial seed [79, ]
1. For each seed in seeds where seed is a list [79, ]
    for each map
        run a function that takes a map and returns a target
            for each path
                destination, source, span = path
                if seed[-1] in combined range(max_lower, min_upper)
                    target = destination - source + seed[-1]
                    seed.append(target)
                    return target
        if target not returned we will append the same value to our seed chain
            seed.append(seed[-1])
2. Once we get through each seed we should have a list of seeds with seed[-1] pointing at location
    extract the min location
    min([seed[-1] for seed in seeds])

## Part 2: Mutlirange
I tried brut and reverse brut approach starting from locations first however none of them worked on input data. 
It seems that the algorithm needs to be improved to work with ranges in a more efficient way. Unfortunately unable to solve part 2 yet.