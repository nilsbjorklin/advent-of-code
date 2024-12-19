import re


def read_data(input_data):
    result = []
    for line in input_data:
        result.append(re.compile(r'\d').findall(line))
    return result


def run(input_data: list[str]):
    data = read_data(input_data)
    result = 0
    for row in data:
        result += int(row[0] + row[len(row) - 1])
    return result


if __name__ == '__main__':
    print(run(open('src/2024/data/days/01/data', 'r').readlines()))
