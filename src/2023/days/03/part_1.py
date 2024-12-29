import itertools
import re


def read_data(input_data):
    digits = {}
    symbols = set()
    pattern = re.compile(r"\d+|[^\.]")
    directions = set(map(lambda xy: xy[0]+xy[1], itertools.product([1, 0, -1], [1j, 0, -1j])))
    for index, row in enumerate(input_data.strip().splitlines()):
        for digit_match in pattern.finditer(row):
            start, end = digit_match.span(0)
            if digit_match.group(0).isdigit():
                positions = set()
                for x in range(start, end):
                    positions.add(complex(x, index))
                digits[tuple(positions)] = int(digit_match.group(0))
            else:
                for direction in directions:
                    symbols.add(complex(start, index) + direction)
    return digits, symbols


def run(input_data: list[str]):
    digits, symbols = read_data(input_data)
    result = 0
    for positions, value in digits.items():
        for pos in positions:
            if pos in symbols:
                result += value
                break
    return result


if __name__ == "__main__":
    print(run(open("src/2023/data/days/03/data", "r").read()))
