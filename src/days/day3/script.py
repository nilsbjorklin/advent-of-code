import re

from src.days.template import Template


class Day3(Template):
    def __init__(self, parse_data, data=0):
        super().__init__(3, self.__func, parse_data, data)

    @staticmethod
    def part_1(data=0):
        return Part1(data)

    @staticmethod
    def part_2(data=0):
        return Part2(data)

    def __func(self):
        result = 0
        for (x, y) in self.data:
            result += x * y
        return result


class Part1(Day3):
    def __init__(self, data=0):
        super().__init__(self.parse_data, data)

    @staticmethod
    def parse_data(data):
        result = []
        for line in data:
            for pair in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line):
                result.append((int(pair[0]), int(pair[1])))
        return result


class Part2(Day3):
    def __init__(self, data=0):
        super().__init__(self.parse_data, data)

    @staticmethod
    def parse_data(data):
        result = []
        instructions_enabled = True
        for line in data:
            pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")
            for match in pattern.finditer(line):
                if instructions_enabled:
                    if match.groups()[3] is not None:
                        instructions_enabled = False
                    elif match.groups()[2] is None:
                        result.append((int(match.group(1)), int(match.group(2))))
                elif match.groups()[2] is not None:
                    instructions_enabled = True
        return result
