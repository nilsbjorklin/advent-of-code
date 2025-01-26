from functools import reduce


directions = [1, -1, 1j, -1j]
values = {}


def read_data(input_data):
    global values
    for y, line in enumerate(input_data.splitlines()):
        for x, val in enumerate(line):
            values[complex(x, y)] = int(val)


def run(input_data: str):
    read_data(input_data)
    low_points = [pos for pos in values.keys() if check_low_point(pos)]
    basins = sorted([calculate_basin(low_point) for low_point in low_points])
    return reduce(lambda a, b: a*b, basins[-3:], 1)


def check_low_point(pos):
    for direction in directions:
        neighbor = pos + direction
        if neighbor in values and values[pos] >= values[neighbor]:
            return False
    return True


def calculate_basin(pos, visited=None):
    if visited is None:
        visited = set()
    visited.add(pos)
    value = values[pos]
    for direction in directions:
        neighbor = pos + direction
        if neighbor not in visited:
            if neighbor in values:
                if values[neighbor] != 9 and value < values[neighbor]:
                    calculate_basin(neighbor, visited)
    return len(visited)


if __name__ == "__main__":
    print(run(open("src/2021/data/days/09/data", "r").read()))
