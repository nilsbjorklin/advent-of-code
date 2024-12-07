import itertools
from typing import Iterable

from src.days.template import Template


def parse_data(data):
    result = []
    max_number_of_values = 0
    for row in data:
        total, values = row.split(':')
        values = [int(num) for num in values.strip().split(' ')]
        max_number_of_values = max(max_number_of_values, len(values))
        result.append((int(total), values))
    return result, max_number_of_values


def operator_combinations(keys: range, options: Iterable):
    result = {}
    for i in keys:
        result[i + 1] = []
        for operator in list(itertools.product(options, repeat=i)):
            result[i + 1].append(list(operator))
    return result


def calculate(row, operators):
    target, values = row
    if values[0] > target: return 0
    if not operators: return values[0]

    return calculate((target, [operators[0](values[0], values[1])] + values[2:]), operators[1:])


class Day7(Template):
    def __init__(self, func, data=0):
        super().__init__(7, func, parse_data, data)

    @staticmethod
    def part_1(data=0):
        return Part1(data)

    @staticmethod
    def part_2(data=0):
        return Part2(data)


class Part1(Day7):
    def __init__(self, data=0):
        super().__init__(self.__func, data)
        self.combs = operator_combinations(range(1, self.data[1]), [lambda a, b: a + b, lambda a, b: a * b])

    def __func(self):
        result = 0
        for row in self.data[0]:
            result += next((res for comb in self.combs[len(row[1])] if (res := calculate(row, comb)) == row[0]), 0)
        return result


class Part2(Day7):
    def __init__(self, data=0):
        super().__init__(self.__func, data)
        self.combs = operator_combinations(range(1, self.data[1]), [
            lambda a, b: a + b,
            lambda a, b: a * b,
            lambda a, b: int(f"{a}{b}")
        ])

    def __func(self):
        result = 0

        for row in self.data[0][:50]:
            result += next((res for comb in self.combs[len(row[1])] if (res := calculate(row, comb)) == row[0]), 0)
        return result
