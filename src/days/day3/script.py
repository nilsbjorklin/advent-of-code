import re

from src.days.template import Template


def fetch_data():
    f = open('data/days/day3/data', 'r')
    data = []
    for line in f.readlines():
        regex = "mul\\((\\d{1,3}),(\\d{1,3})\\)"
        for result in re.findall(regex, line):
            data.append((int(result[0]), int(result[1])))
    return data


class Day3(Template):
    def __init__(self, func, data=0):
        data = data if data != 0 else fetch_data()
        super().__init__(1, func, data)

    @staticmethod
    def part_1(data=0):
        return Part1(data)

    @staticmethod
    def part_2(data=0):
        return Part2(data)


class Part1(Day3):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

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
