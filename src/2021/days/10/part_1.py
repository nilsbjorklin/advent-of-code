def read_data(input_data):
    point_map = {"(": 3, ")": -3, "[": 57, "]": -57, "{": 1197, "}": -1197, "<": 25137, ">": -25137}
    return [[point_map[char] for char in line] for line in input_data.splitlines()]


def run(input_data: str):
    lines = read_data(input_data)
    return sum([line_result(line) for line in lines])

def line_result(line):
    values = []
    for val in line:
        if val > 0:
            values.append(val)
        else:
            if values.pop(-1) + val != 0:
                return -val
    return 0

if __name__ == "__main__":
    print(run(open("src/2021/data/days/10/data", "r").read()))
