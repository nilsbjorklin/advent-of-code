import numpy as np


def read_data(input_data):
    return np.array([[int(num) for num in row] for row in input_data.splitlines()])


def run(input_data):
    tree_rows = read_data(input_data)
    tree_cols = np.swapaxes(tree_rows, 0, 1)
    trees_seen = 0
    for row_idx, row in enumerate(tree_rows):
        for col_idx, tree in enumerate(row):
            if row_idx == 0 or col_idx == 0:
                trees_seen += 1
            elif row_idx + 1 == len(tree_rows) or col_idx + 1 == len(row):
                trees_seen += 1
            else:
                row_before = max(row[:col_idx])
                row_after = max(row[col_idx + 1 :])
                col_before = max(tree_cols[col_idx][:row_idx])
                col_after = max(tree_cols[col_idx][row_idx + 1 :])
                lowest_path = min(row_before, row_after, col_before, col_after)
                if lowest_path < tree:
                    trees_seen += 1
    return trees_seen


if __name__ == "__main__":
    print(run(open("src/2022/data/days/08/data", "r").read()))
