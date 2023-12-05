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
I think it will be easier to start from symbols. We will go over symbol neighbours and adjesent number and its number neighbours.

1. Create a structure map of zeros - grid len(line in data) x len(data.split())
2. Check the (i,j) of symbols in the data.
3. Pass this (i,j) as parameters to neighbours function that returns (x,y) of a neighbour that is a number
    - Update the map with 1 for (x,y)
    - Pass (x,y) as parameters to neighbours function
4. Continue to the next number when neighbours completed running

The resulting map will consist of 1s and mark location of numbers we need.

1. For i,j of each element of a map that is 1 fetch i,j and join to number
    - If next i,j is not 1 then append number to a list and set number to ''
2. Sum int values from the returned list