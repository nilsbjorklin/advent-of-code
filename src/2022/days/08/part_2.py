import numpy as np


def read_data(input_data):
    return np.array([[int(num) for num in row] for row in input_data.splitlines()])


def run(input_data):
    tree_rows = read_data(input_data)
    tree_cols = np.swapaxes(tree_rows, 0, 1)
    max_scenic_score = 0
    for row_idx, row in enumerate(tree_rows):
        for col_idx, tree in enumerate(row):
            tree_directions = [
                row[:col_idx][::-1],
                row[col_idx + 1 :],
                tree_cols[col_idx][:row_idx][::-1],
                tree_cols[col_idx][row_idx + 1 :],
            ]
            scenic_score = 1
            for tree_direction in tree_directions:
                distance = 0
                for next_tree in tree_direction:
                    distance += 1
                    if next_tree >= tree:
                        break
                scenic_score *= distance
            max_scenic_score = max(scenic_score, max_scenic_score)
    return max_scenic_score


if __name__ == "__main__":
    print(run(open("src/2022/data/days/08/data", "r").read()))
