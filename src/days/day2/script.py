import copy

from src.days.template import Template


def fetch_data():
    f = open('data/days/day2/data', 'r')
    data = []
    for line in f.readlines():
        parts = line.strip().split()
        data.append([int(part) for part in parts])
    return data


class Day2(Template):
    def __init__(self, func, data=0):
        data = data if data != 0 else fetch_data()
        super().__init__(1, func, data)

    @staticmethod
    def part_1(data=0):
        return Part1(data)

    @staticmethod
    def part_2(data=0):
        return Part2(data)


class Part1(Day2):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    @staticmethod
    def difference_is_invalid(val1, val2):
        return abs(val2 - val1) > 3

    @staticmethod
    def list_is_valid(lst):
        if Part1.is_sorted_ascending(lst) or Part1.is_sorted_descending(lst):
            for i in range(len(lst) - 1):
                if Part1.difference_is_invalid(lst[i], lst[i + 1]):
                    return False
            return True
        else:
            return False

    @staticmethod
    def is_sorted_ascending(lst):
        return all(
            lst[index] < lst[index + 1]
            for index in range(len(lst) - 1)
        )

    @staticmethod
    def is_sorted_descending(lst):
        return all(
            lst[index] > lst[index + 1]
            for index in range(len(lst) - 1)
        )

    def __func(self):
        safe_report_count = 0
        for report in self.data:
            if Part1.list_is_valid(report): safe_report_count += 1
        return safe_report_count


class Part2(Day2):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    @staticmethod
    def tuple_is_invalid(num, prev_num, direction):
        if num == prev_num:
            return True
        elif ((prev_num - num) > 0) == direction:
            return True
        elif abs(prev_num - num) > 3:
            return True
        return False

    @staticmethod
    def calculate_direction(lst):
        average_direction_sum = 0
        for i in range(1, len(lst)):
            average_direction_sum += lst[i] - lst[i - 1]
        return average_direction_sum > 0

    @staticmethod
    def list_is_valid(lst, remove_index=None):
        modified_list = copy.deepcopy(lst)
        if remove_index is not None:
            del modified_list[remove_index]
        direction = Part2.calculate_direction(modified_list)
        suspected_indexes = []

        for i in range(1, len(modified_list)):
            if Part2.tuple_is_invalid(modified_list[i], modified_list[i - 1], direction):
                suspected_indexes.append(i)
                suspected_indexes.append(i - 1)

        if len(suspected_indexes) != 0 and remove_index is None:
            suspected_indexes = list(set(suspected_indexes))
            for i in suspected_indexes:
                if Part2.list_is_valid(modified_list, i):
                    return True
            return False
        else:
            return len(suspected_indexes) == 0

    def __func(self):
        safe_report_count = 0
        for report in self.data:
            if Part2.list_is_valid(report): safe_report_count += 1
        return safe_report_count
