from collections import defaultdict

import numpy as np


def read_data(input_data):
    result = defaultdict(set)
    for row_idx, row in enumerate(input_data):
        for col_idx, col in enumerate(row.strip()):
            if col == "A":
                if 0 >= row_idx >= len(input_data) - 1:
                    if 0 >= col_idx >= len(row) - 1:
                        break
            result[col].add(col_idx + row_idx * 1j)
    return result


def run(input_data: list[str]):
    corners = ["M", "M", "S", "S"]
    modifiers = [(-1 - 1j), (1 - 1j), (1 + 1j), (-1 + 1j)]
    xmas_found = 0
    data = read_data(input_data)
    for val in data["A"]:
        for i in range(4):
            valid_perm = True
            corners = np.roll(corners, 1)
            for mod_idx, modifier in enumerate(modifiers):
                if val + modifier not in data[corners[mod_idx]]:
                    valid_perm = False
            if valid_perm:
                xmas_found += 1
                break
    return xmas_found


if __name__ == "__main__":
    print(run(open("src/2024/data/days/04/data", "r").readlines()))
