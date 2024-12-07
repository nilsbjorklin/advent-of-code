from collections.abc import Callable

from src.days.template import Template


def parse_data(data):
    result = []
    for row in data:
        total, values = row.split(':')
        values = [int(num) for num in values.strip().split(' ')]
        result.append((int(total), values))
    return result


def calculate_values(target: int,
                     values: list[int],
                     value_builder: Callable[[int, int], list[int]],
                     total: int = 0) -> int:
    values_to_try: list[int] = []
    if not values:
        return target if target == total else 0
    elif total > target:
        return 0
    elif not total:
        values_to_try.append(values[0])
    else:
        values_to_try = value_builder(total, values[0])
    for value in values_to_try:
        res = calculate_values(target, values[1:], value_builder, value)
        if res:
            return res
    return 0


class Day7(Template):
    def __init__(self, value_builder, data=0):
        super().__init__(7, self.__func, parse_data, data)
        self.value_builder = value_builder

    @staticmethod
    def part_1(data=0):
        return Part1(data)

    @staticmethod
    def part_2(data=0):
        return Part2(data)

    def __func(self):
        result = 0
        for target, values in self.data:
            result += calculate_values(target, values, self.value_builder)
        return result


class Part1(Day7):
    def __init__(self, data=0):
        super().__init__(self.value_builder, data)

    @staticmethod
    def value_builder(total: int, value: int) -> list[int]:
        return [total + value, total * value]


class Part2(Day7):
    def __init__(self, data=0):
        super().__init__(self.value_builder, data)

    @staticmethod
    def value_builder(total: int, value: int) -> list[int]:
        return [total + value, total * value, int(f"{total}{value}")]
