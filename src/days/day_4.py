import itertools

from src.days.template import Template


class Day4(Template):
    def __init__(self, func, parse_data, data=0):
        super().__init__(4, func, parse_data, data)

    @staticmethod
    def part_1(data=0):
        return Part1(data)

    @staticmethod
    def part_2(data=0):
        return Part2(data)


class Part1(Day4):
    def __init__(self, data=0):
        super().__init__(self.__func, self.parse_data, data)

    @staticmethod
    def parse_data(data):
        result = {
            'X': [],
            'M': [],
            'A': [],
            'S': []
        }
        for (row_idx, row) in enumerate(data):
            for (col_idx, col) in enumerate(row.strip()):
                result.get(col).append((row_idx, col_idx))
        for key in result.keys():
            result[key] = set(result.get(key))
        return result

    def __func(self):
        combinations = list(itertools.product([0, 1, -1], repeat=2))[1:]
        xmas_found = 0

        for val in self.data['X']:
            for combination in combinations:
                if self.check_xmas(val[0], val[1], col_change=combination[0], row_change=combination[1]):
                    xmas_found += 1
        return xmas_found

    def check_xmas(self, row, col, row_change=0, col_change=0):
        if (row + row_change, col + col_change) in self.data['M']:
            if (row + row_change * 2, col + col_change * 2) in self.data['A']:
                if (row + row_change * 3, col + col_change * 3) in self.data['S']:
                    return True
        return False


class Part2(Day4):
    def __init__(self, data=0):
        super().__init__(self.__func, self.parse_data, data)

    @staticmethod
    def parse_data(data):
        result = {
            1: [],
            0: [],
            -1: []
        }
        for (row_idx, row) in enumerate(data):
            for (col_idx, col) in enumerate(row.strip()):
                match col:
                    case 'M':
                        result[1].append((row_idx, col_idx))
                    case 'A':
                        if row_idx != 0 and col_idx != 0:
                            if row_idx != len(data) - 1 and col_idx != len(row) - 1:
                                result[0].append((row_idx, col_idx))
                    case 'S':
                        result[-1].append((row_idx, col_idx))
        for key in result.keys():
            result[key] = set(result.get(key))
        return result

    def __func(self):
        combinations = list(itertools.product([1, -1], repeat=2))
        xmas_found = 0
        for val in self.data[0]:
            for combination in combinations:
                if self.check_mas_mas(val[0], val[1], combination):
                    xmas_found += 1
        return xmas_found

    def check_mas_mas(self, row, col, combination):
        first_corner = (row - 1, col - 1)
        second_corner = (row - 1, col + 1)
        third_corner = (row + 1, col + 1)
        fourth_corner = (row + 1, col - 1)
        if first_corner in self.data[combination[0]]:
            if second_corner in self.data[combination[1]]:
                if third_corner in self.data[combination[0] * -1]:
                    if fourth_corner in self.data[combination[1] * -1]:
                        return True
        return False
