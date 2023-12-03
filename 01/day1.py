from pathlib import Path
import time


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

    print('Part 1:', sum([calibration_values(line, numbers) for line in data]))
    print("--- %s seconds ---" % (time.time() - start_time))