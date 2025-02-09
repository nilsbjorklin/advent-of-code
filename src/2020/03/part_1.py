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
    path = {((y * 3) % width, y) for y in range(height + 1)}
    return len(path.intersection(trees))


if __name__ == "__main__":
    print(run(open("data", "r").read()))
