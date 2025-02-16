import re
from functools import lru_cache

pattern = re.compile(r"(\d+|\+|\*)")


def read_data(input_data: str) -> list:
    return [line.replace(" ", "") for line in input_data.splitlines()]


def run(input_data: str) -> int:
    lines = read_data(input_data)
    result = 0
    for line in lines:
        while "(" in line:
            start_index = index = 0
            end_index = len(line) - 1
            while index <= end_index:
                char = line[index]
                if char == "(":
                    start_index = index + 1
                elif char == ")":
                    end_index = index
                index += 1
            before, segment, after = (
                line[: start_index - 1],
                line[start_index:end_index],
                line[end_index + 1:],
            )
            line = before + str(calculate_segment(segment)) + after
        result += calculate_segment(line)
    return result


@lru_cache
def calculate_segment(segment):
    segment = pattern.findall(segment)
    while len(segment) != 1:
        index = segment.index("+") if "+" in segment else segment.index("*")
        segment[index - 1] = str(calculate_expression(*segment[index - 1: index + 2]))
        del segment[index]
        del segment[index]
    return int(segment[0])


@lru_cache
def calculate_expression(first, operator, second):
    return int(first) * int(second) if operator == "*" else int(first) + int(second)


if __name__ == "__main__":
    print(run(open("data", "r").read()))
