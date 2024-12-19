import re

import numpy as np


def read_data(input_data):
    pattern = re.compile(r"\w=(-?\d+),(-?\d+)")
    robots_pos = []
    robots_move = []
    for row in input_data:
        pos, move = row.split(" ")
        robots_pos.append(
            np.array([int(val) for val in re.match(pattern, pos).groups()])
        )
        robots_move.append(
            np.array([int(val) for val in re.match(pattern, move).groups()])
        )
    return np.array(robots_pos), np.array(robots_move)


def run(input_data, size):
    robots_pos, robots_move = read_data(input_data)

    max_col, max_row, max_both = [0, 0, 0]
    result = robots_pos
    found = 0
    for iteration in range(10000):
        for i in range(size[1]):
            col_count = len(result[np.nonzero(result[:, 0] == i)[0]])
            row_count = len(result[np.nonzero(result[:, 1] == i)[0]])
            if (col_count + row_count) > max_both:
                max_both = col_count + row_count
                print(f"Max both at {iteration}")
                found = iteration
        result = np.mod(np.add(result, robots_move), size)
    print_space(np.mod(np.add(robots_pos, np.multiply(robots_move, found)), size), size)
    return found


def print_space(positions, size):
    result = np.zeros(tuple(size), dtype=int)
    for pos in positions:
        result[tuple(pos)] += 1
    result = np.strings.replace(result.astype(dtype=str), "0", ".")
    print("\n", "\n".join(["".join(row) for row in np.transpose(result)]))


if __name__ == "__main__":
    print(run(open("src/2024/data/days/14/data", "r").readlines(), [101, 103]))
