from copy import copy
import numpy as np


def read_data(input_data, decryption_key):
    return [
        (index, value)
        for index, value in enumerate(
            np.multiply(
                [int(row.strip()) for row in input_data.splitlines()], decryption_key
            )
        )
    ]


def run(input_data, decryption_key):
    numbers = read_data(input_data, decryption_key)
    original = copy(numbers)
    for _ in range(10):
        for number in original:
            index = numbers.index(number)
            value = numbers.pop(index)
            numbers.insert((index + value[1]) % len(numbers), value)

    numbers = list(map(lambda x: x[1], numbers))
    zero_index = numbers.index(0)
    return sum(
        [numbers[(i + zero_index) % len(numbers)] for i in range(1000, 3001, 1000)]
    )


if __name__ == "__main__":
    print(run(open("src/2022/data/days/20/data", "r").read(), 811589153))
