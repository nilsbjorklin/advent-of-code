from functools import lru_cache
from math import ceil

lower = {"F", "L"}


def read_data(input_data):
    return [
        [char in lower for char in line] for line in input_data.strip().splitlines()
    ]


def run(input_data):
    boarding_passes = read_data(input_data)
    return max(
        [
            calculate_value(splits[:7], 127) * 8 + calculate_value(splits[7:], 7)
            for splits in boarding_passes
        ]
    )


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
