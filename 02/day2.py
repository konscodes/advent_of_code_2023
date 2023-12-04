from pathlib import Path
import time

if __name__ == '__main__':
    # Start the timer
    start_time = time.time()

    # Set filepath
    script_path = Path(__file__).resolve()
    file_path = script_path.parent / 'test.txt'

    with open(file_path) as f:
        # Split the data into list of strings
        data = f.read().splitlines()

    print(data)
    
    print('Part 1:')
    print('Part 2:')
    print("--- %s seconds ---" % (time.time() - start_time))
