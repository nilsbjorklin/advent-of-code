from functools import reduce


def read_data(input_data):
    lines = input_data.splitlines()
    trees = {
        (x, y)
        for y, row in enumerate(lines)
        for x, char in enumerate(row)
        if char == "#"
    }
    return trees, len(lines[0]), len(lines)


def run(input_data):
    trees, width, height = read_data(input_data)
    directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    paths = [
        len(
            [
                1
                for idx in range(height + 1)
                if ((idx * x_mod) % width, idx * y_mod) in trees
            ]
        )
        for x_mod, y_mod in directions
    ]
    return reduce(lambda a, b: a * b, paths, 1)


if __name__ == "__main__":
    print(run(open("data", "r").read()))
