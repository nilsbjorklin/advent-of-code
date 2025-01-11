import numpy as np

def read_data(input_data):
    rucksacks = [set(row) for row in input_data.splitlines()]
    return np.split(rucksacks, np.arange(3, len(rucksacks), 3))


def run(input_data: list[str]):
    groups = read_data(input_data)
    overlap_sum = 0
    for first, second, third in groups:
        char_val = ord(first.intersection(second).intersection(third).pop())
        char_val -= 38 if char_val < 97 else 96
        overlap_sum += char_val
    return overlap_sum


if __name__ == "__main__":
    print(run(open("src/2022/data/days/03/data", "r").read()))
