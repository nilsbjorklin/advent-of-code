from collections import defaultdict
from copy import deepcopy

data = defaultdict(set)
data_array = []
paths = defaultdict(list)
width = height = 0
directions = [1, -1, 1j, -1j]


def read_data(input_data):
    global data
    global width
    global height
    width = len(input_data[0])
    height = len(input_data)
    for y, row in enumerate(input_data):
        for x, value in enumerate(row.strip()):
            if value != '.':
                data[int(value)].add(x + y * 1j)


def run(input_data: list[str]):
    read_data(input_data)

    return connections()


def connections(path=None, parent=None, incline=0):
    if parent is None:
        total = 0
        for idx, value in enumerate(data[0]):
            total_for_node = connections([value], value, incline + 1)
            total += total_for_node
        return total
    if incline > 9:
        return 1
    else:
        total = 0
        for node in data[incline]:
            if parent - node in directions:
                new_path = deepcopy(path)
                new_path.append(node)
                total += connections(new_path, node, incline + 1)
        return total


if __name__ == '__main__':
    print(run(open('../../data/days/10/data', 'r').readlines()))
