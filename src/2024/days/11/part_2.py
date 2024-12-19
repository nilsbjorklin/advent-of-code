import math
from collections import defaultdict

import numpy as np

number_lookup = defaultdict(list[int])


def read_data(input_data):
    stones = defaultdict(lambda: 0)
    for stone in input_data[0].split(' '):
        stones[int(stone)] += 1
    return stones


def run(input_data: list[str], num_blinks):
    stones = read_data(input_data)

    for _ in range(num_blinks):
        new_stones = defaultdict(lambda: 0)
        for val, amount in stones.items():
            for value in next_step(val):
                new_stones[value] += amount
        stones = new_stones

    return np.sum(list(stones.values()))


def next_step(stone):
    global number_lookup
    if stone not in number_lookup:
        if stone == 0:
            number_lookup[stone] = [1]
        else:
            num_len = int(math.log10(stone)) + 1
            if num_len % 2 == 0:
                number_lookup[stone] = list(divmod(stone, 10 ** int(num_len / 2)))
            else:
                number_lookup[stone] = [stone * 2024]
        return number_lookup[stone]
    return number_lookup[stone]


if __name__ == '__main__':
    print(run(open('src/2024/data/days/11/data', 'r').readlines(), 75))
