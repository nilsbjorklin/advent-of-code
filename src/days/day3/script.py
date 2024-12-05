import re

from src.days.template import Template


class Day3(Template):
    def __init__(self, func, parse_data, data=0):
        super().__init__(1, func, parse_data, data)

    @staticmethod
    def part_1(data=0):
        return Part1(data)

    @staticmethod
    def part_2(data=0):
        return Part2(data)


class Part1(Day3):
    def __init__(self, data=0):
        super().__init__(self.__func, self.parse_data, data)

    @staticmethod
    def parse_data(data):
        result = []
        for line in data:
            regex = "mul\\((\\d{1,3}),(\\d{1,3})\\)"
            for pair in re.findall(regex, line):
                result.append((int(pair[0]), int(pair[1])))
        return result

    def __func(self):
        result = 0
        for (x, y) in self.data:
            result += x * y
        return result


class Part2(Day3):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def __func(self):
        pass
