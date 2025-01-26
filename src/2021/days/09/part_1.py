from collections import defaultdict

directions = [1, -1, 1j, -1j]

def read_data(input_data):
    values = {}
    for y, line in enumerate(input_data.splitlines()):
        for x, val in enumerate(line):
            values[complex(x, y)] = int(val)
    return values


def run(input_data: str):
    values = read_data(input_data)
    return sum([value+1 for pos, value in values.items() if check_low_point(pos, value, values)])

def check_low_point(pos, value, values):
    for direction in directions:
        neighbor = pos + direction
        if neighbor in values and value >= values[neighbor]:
            return False
    return True

if __name__ == "__main__":
    print(run(open("src/2021/data/days/09/data", "r").read()))
