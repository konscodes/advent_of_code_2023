from pathlib import Path
import time

def get_first(line: str):
    first = ''
    for char in line:
        if char in numbers:
            return str(char)
        first += char
        for index, string in enumerate(strings):
            if string in first:
                return str(index)
    return 'NA'


def get_last(line: str):
    last = ''
    for char in line[::-1]:
        if char in numbers:
            return str(char)
        last += char
        for index, string in enumerate(strings):
            if string in last[::-1]:
                return str(index)
    return 'NA'


def calibration_values_ws(line: str, numbers: list, strings: list[str]) -> int:
    '''Return a combination of first and last digit from a given string.'''
    first = get_first(line)
    last = get_last(line)
    return int(first + last)


def calibration_values(line: str, numbers: list) -> int:
    '''Return a combination of first and last digit from a given string.'''
    filtered = [char for char in line if char in numbers]
    first = filtered[0]
    last = filtered[-1]
    return int(first + last)


if __name__ == '__main__':
    # Start the timer
    start_time = time.time()

    # Set filepath
    script_path = Path(__file__).resolve()
    file_path = script_path.parent / 'day1.txt'

    with open(file_path) as f:
        # Split the data into list of strings
        data = f.read().splitlines()
    
    # Create list of numbers to compare against
    numbers = [x for x in '1234567890']
    strings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    print('Part 1:', sum([calibration_values(line, numbers) for line in data]))
    print('Part 2:', sum([calibration_values_ws(line, numbers, strings) for line in data]))
    print("--- %s seconds ---" % (time.time() - start_time))