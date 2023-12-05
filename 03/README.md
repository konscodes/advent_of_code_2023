# [Day 3: Gear Ratios](https://adventofcode.com/2023/day/3)

## Part1: Part numbers (any number adjacent to a symbol)
Here is an example engine schematic:

```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

### Thoughts
I think it will be easier to start from symbols. We will go over symbol neighbors and adjacent number and its number neighbors.

1. Create a structure map of zeros - grid len(line in data) x len(data.split())
2. Check the (i,j) of symbols in the data.
3. Pass this (i,j) as parameters to neighbors function that returns (x,y) of a neighbor that is a number
    - Update the map with 1 for (x,y)
    - Pass (x,y) as parameters to neighbors function
4. Continue to the next number when neighbors completed running

The resulting map will consist of 1s and mark location of numbers we need.

1. For i,j of each element of a map that is 1 fetch i,j and join to number
    - If next i,j is not 1 then append number to a list and set number to ''
2. Sum int values from the returned list

## Part 2: Gear ratios for all * gears adjacent to two numbers
The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.