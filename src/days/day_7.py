from src.days.template import Template


def parse_data(data):
    return data


class Day7(Template):
    def __init__(self, func, data=0):
        super().__init__(6, func, parse_data, data)

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
        pass


class Part2(Day7):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def __func(self):
        pass
