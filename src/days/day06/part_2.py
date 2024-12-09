from copy import deepcopy


def read_data(input_data):
    obstacles: set[complex] = set()
    row_limit = len(input_data)
    col_limit = len(input_data[0].strip())
    pos: complex = 0 + 0j
    for (row_idx, row) in enumerate(input_data):
        for (col_idx, val) in enumerate(row):
            if val == '#':
                obstacles.add(col_idx + row_idx * 1j)
            elif val == '^':
                pos = col_idx + row_idx * 1j
    return pos, obstacles, row_limit, col_limit


def run(input_data: list[str]):
    data = read_data(input_data)
    pos1, obstacles1, height1, width1 = deepcopy(data)
    direction = -1j
    path1 = []
    while 0 <= pos1.real < width1 and 0 <= pos1.imag < height1:
        if pos1 + direction in obstacles1:
            direction *= 1j
        else:
            pos1 += direction
            if pos1 not in path1:
                path1.append(pos1)
    path = path1
    pos, obstacles, height, width = data
    num_obstacles = 0
    for i, location in enumerate(path):
        new_obstacles = deepcopy(obstacles)
        new_obstacles.add(location)
        if check_looping(pos, new_obstacles, height, width):
            num_obstacles += 1
    return num_obstacles


def check_looping(pos, obstacles, height, width):
    direction = -1j
    memory = set()
    dir_count = 0
    while 0 <= pos.real < width and 0 <= pos.imag < height:
        if (pos, direction) in memory:
            return True
        if (pos + direction) in obstacles:
            memory.add((pos, direction))
            direction *= 1j
        else:
            dir_count += 1
            pos += direction
    return False


if __name__ == '__main__':
    print(run(open('../../data/days/06/data', 'r').readlines()))
