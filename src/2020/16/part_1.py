import re
from functools import lru_cache

rules = []


def read_data(input_data: str) -> list:
    global rules
    rules, _, tickets = input_data.split("\n\n")
    pattern = re.compile(r"(\d+)-(\d+)")
    rules = [
        (int(min_value), int(max_value))
        for min_value, max_value in pattern.findall(rules)
    ]
    return [list(map(int, line.split(","))) for line in tickets.splitlines()[1:]]


def run(input_data: str) -> int:
    tickets = read_data(input_data)
    invalid_numbers_sum = 0
    for ticket in tickets:
        for number in ticket:
            if not is_valid(number):
                invalid_numbers_sum += number
    return invalid_numbers_sum


@lru_cache
def is_valid(number):
    for min_value, max_value in rules:
        if min_value <= number <= max_value:
            return True
    return False


if __name__ == "__main__":
    print(run(open("data", "r").read()))
