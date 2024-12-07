import itertools

from src.days.template import Template


def parse_data(data):
    result = []
    operators = {}
    max_number_of_values = 0
    for row in data:
        total, values = row.split(':')
        values = [int(num) for num in values.strip().split(' ')]
        max_number_of_values = max(max_number_of_values, len(values))
        result.append((int(total), values))
    for i in range(1, max_number_of_values):
        operators[i + 1] = []
        for operator in list(itertools.product('*+', repeat=i)):
            operators[i + 1].append(list(operator))
    return result, operators


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

    def __func(self):
        operators_combinations_list = self.data[1]
        result = 0
        for row in self.data[0]:
            result += next((res for operators in operators_combinations_list[len(row[1])] if
                            (res := self.calculate(row, operators)) == row[0]), 0)
        return result

    def calculate(self, row, operators):
        target, values = row

        if values[0] > target: return 0
        if not operators: return values[0]

        return self.calculate((target, [eval(f"{values[0]} {operators[0]} {values[1]}")] + values[2:]), operators[1:])


class Part2(Day7):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def __func(self):
        pass
