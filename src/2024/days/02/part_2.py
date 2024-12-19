import copy

import numpy as np


def read_data(input_data):
    result = []
    for line in input_data:
        parts = line.strip().split()
        result.append([int(part) for part in parts])
    return result


def run(input_data: list[str]):
    safe_report_count = 0
    for report in read_data(input_data):
        if list_is_valid(report): safe_report_count += 1
    return safe_report_count


def list_is_valid(lst, remove_index=None):
    modified_list = copy.deepcopy(lst)
    if remove_index is not None:
        del modified_list[remove_index]
    valid_range = range(1, 4) if np.diff(modified_list).sum() > 0 else range(-3, 0)
    suspected_indexes = set()

    for i in range(1, len(modified_list)):
        if modified_list[i] - modified_list[i - 1] not in valid_range:
            suspected_indexes.update([i, i - 1])

    if remove_index is None:
        for i in suspected_indexes:
            if list_is_valid(modified_list, i): return True
    return not bool(suspected_indexes)


if __name__ == '__main__':
    print(run(open('src/2024/data/days/02/data', 'r').readlines()))
