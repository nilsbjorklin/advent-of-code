from functools import reduce


def read_data(input_data):
    point_map = {"(": 1, ")": -1, "[": 2, "]": -2, "{": 3, "}": -3, "<": 4, ">": -4}
    return [[point_map[char] for char in line] for line in input_data.splitlines()]


def run(input_data: str):
    lines = read_data(input_data)
    result = [result for result in [line_result(line) for line in lines] if result != 0]
    return sorted(result)[len(result) // 2]


def line_result(line):
    values = []
    for val in line:
        if val > 0:
            values.append(val)
        else:
            if values.pop(-1) + val != 0:
                return 0
    return reduce(lambda res, val: res * 5 + val, values[::-1], 0)


if __name__ == "__main__":
    print(run(open("src/2021/data/days/10/data", "r").read()))
