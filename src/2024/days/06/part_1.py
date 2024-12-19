def read_data(input_data):
    obstacles: set[complex] = set()
    row_limit = len(input_data)
    col_limit = len(input_data[0].strip())
    pos: complex = 0 + 0j
    for row_idx, row in enumerate(input_data):
        for col_idx, val in enumerate(row):
            if val == "#":
                obstacles.add(col_idx + row_idx * 1j)
            elif val == "^":
                pos = col_idx + row_idx * 1j
    return pos, obstacles, row_limit, col_limit


def run(input_data: list[str]):
    pos, obstacles, height, width = read_data(input_data)
    direction = -1j
    path = set()
    while 0 <= pos.real < width and 0 <= pos.imag < height:
        if pos + direction in obstacles:
            direction *= 1j
        else:
            path.add(pos)
            pos += direction
    return len(set(path))


if __name__ == "__main__":
    print(run(open("src/2024/data/days/06/data", "r").readlines()))
