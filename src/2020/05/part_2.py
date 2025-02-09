from collections import defaultdict
from functools import lru_cache
from math import ceil

lower = {"F", "L"}


def read_data(input_data):
    return [
        [char in lower for char in line] for line in input_data.strip().splitlines()
    ]


def run(input_data):
    boarding_passes = read_data(input_data)
    seats = defaultdict(list)
    for splits in boarding_passes:
        seats[calculate_value(splits[:7], 127)].append(calculate_value(splits[7:], 7))
    seat_numbers = set(range(8))
    for row_number in sorted(seats.keys())[1:-1]:
        missing_seats = seat_numbers.difference(seats[row_number])
        if missing_seats:
            return row_number * 8 + list(missing_seats)[0]


def calculate_value(splits, max_value):
    min_value = 0
    for split in splits:
        min_value, max_value = lower_or_upper(min_value, max_value, split)
    return min_value


@lru_cache
def lower_or_upper(min_value, max_value, lower_half=True):
    middle = min_value + (max_value - min_value) / 2
    if lower_half:
        return min_value, int(middle)
    else:
        return ceil(middle), max_value


if __name__ == "__main__":
    print(run(open("data", "r").read()))
