import numpy as np


def read_data(input_data, expansion_size):
    rows = input_data.strip().splitlines()
    grid = np.zeros((len(rows[0].strip()), len(rows)))
    locations = []
    for y, line in enumerate(rows):
        for x, char in enumerate(line.strip()):
            if char == "#":
                grid[y][x] = 1
                locations.append((x, y))
                
    expansion_size -= 1 
    empty_cols = np.multiply(np.add.accumulate(np.sum(grid, axis=0) == 0), expansion_size)
    empty_rows = np.multiply(np.add.accumulate(np.sum(grid, axis=1) == 0), expansion_size)
    
    for index, location in enumerate(locations):
        x, y = location
        locations[index] = x + empty_cols[x], y + empty_rows[y]

    return locations


def run(input_data, expansion_size):
    locations = read_data(input_data, expansion_size)
    pairs = []
    for first in range(len(locations)):
        for second in range(first + 1, len(locations)):
            first_x, first_y = locations[first]
            second_x, second_y = locations[second]
            pairs.append(abs(first_x - second_x) + abs(first_y - second_y))
    return sum(pairs)

if __name__ == "__main__":
    print(run(open("src/2023/data/days/11/data", "r").read(), 1000000))
