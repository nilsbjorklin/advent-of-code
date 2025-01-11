import itertools
from collections import defaultdict


def read_data(input_data):
    result = defaultdict(list)
    for height_idx, row in enumerate(input_data):
        for width_idx, letter in enumerate(row.strip()):
            if letter != ".":
                result[letter].append(width_idx + height_idx * 1j)
    return result, len(input_data[0]), len(input_data)


def run(input_data: list[str]):
    data, width, height = read_data(input_data)
    nodes = set()
    for k, v in data.items():
        indexes: list[int] = list(range(len(v)))
        for order in list(itertools.permutations(indexes, 2)):
            node = v[order[0]] * 2 - v[order[1]]
            if 0 <= int(node.imag) < height and 0 <= int(node.real) < width:
                nodes.add(node)
    return len(nodes)


if __name__ == "__main__":
    print(run(open("src/2024/data/days/08/data", "r").readlines()))
