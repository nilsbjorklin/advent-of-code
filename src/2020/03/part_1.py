def read_data(input_data):
    trees = set()
    lines = input_data.splitlines()
    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == "#":
                trees.add((x, y))
    return trees, len(lines[0]), len(lines)


def run(input_data):
    trees, width, height = read_data(input_data)
    pos = (0, 0)
    direction = (3, 1)
    result = 0
    print(trees)
    while pos[1] < height:
        pos = ((pos[0] + direction[0]) % width, pos[1] + direction[1])
        if pos in trees:
            result += 1
    return result


if __name__ == "__main__":
    print(run(open("data", "r").read()))
