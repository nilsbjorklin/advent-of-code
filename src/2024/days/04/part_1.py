import itertools
from collections import defaultdict


def read_data(input_data):
    result = defaultdict(set)
    for row_idx, row in enumerate(input_data):
        for col_idx, col in enumerate(row.strip()):
            result[col].add(col_idx + row_idx * 1j)
    return result


def run(input_data: list[str]):
    changes = list(
        map(lambda x: x[0] + x[1], list(itertools.product([0, 1, -1], [0, 1j, -1j])))
    )[1:]
    xmas_found = 0
    data = read_data(input_data)
    for val in data["X"]:
        for change in changes:
            if (val + change) in data["M"]:
                if (val + change * 2) in data["A"]:
                    if (val + change * 3) in data["S"]:
                        xmas_found += 1
    return xmas_found


if __name__ == "__main__":
    print(run(open("src/2024/data/days/04/data", "r").readlines()))
