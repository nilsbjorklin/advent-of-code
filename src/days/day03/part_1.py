import re


def read_data(input_data):
    result = []
    for line in input_data:
        for pair in re.findall(r"mul\((\d{01,03}),(\d{01,03})\)", line):
            result.append((int(pair[0]), int(pair[1])))
    return result


def run(input_data: list[str]):
    result = 0
    for (x, y) in read_data(input_data):
        result += x * y
    return result


if __name__ == '__main__':
    print(run(open('../../data/days/03/data', 'r').readlines()))
