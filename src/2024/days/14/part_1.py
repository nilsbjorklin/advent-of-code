import functools
import re
from collections import defaultdict
from operator import mul

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


def run(input_data, steps, size):
    pos_list, robots_move = read_data(input_data)
    size = size
    middle = np.array(np.array(size) / 2, dtype=int)

    # total step length after all steps
    move = np.multiply(robots_move, steps)
    # add move to initial position and handle overflow
    pos_list = np.mod(np.add(pos_list, move), size)

    result = defaultdict(int)
    for pos in pos_list:
        if pos[0] != middle[0] and pos[1] != middle[1]:
            result[(str(pos[0] > middle[0]), str(pos[1] > middle[1]))] += 1
    return functools.reduce(mul, result.values())


if __name__ == "__main__":
    print(run(open("src/2024/data/days/14/data", "r").readlines(), 100, [101, 103]))
