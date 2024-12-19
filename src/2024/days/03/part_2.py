import re


def read_data(input_data):
    result = []
    instructions_enabled = True
    for line in input_data:
        pattern = re.compile(r"mul\((\d{01,03}),(\d{01,03})\)|(do)\(\)|(don't)\(\)")
        for match in pattern.finditer(line):
            if instructions_enabled:
                if match.groups()[3] is not None:
                    instructions_enabled = False
                elif match.groups()[2] is None:
                    result.append((int(match.group(1)), int(match.group(2))))
            elif match.groups()[2] is not None:
                instructions_enabled = True
    return result


def run(input_data: list[str]):
    result = 0
    for (x, y) in read_data(input_data):
        result += x * y
    return result


if __name__ == '__main__':
    print(run(open('src/2024/data/days/03/data', 'r').readlines()))
