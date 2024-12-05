from src.days.template import Template


def parse_data(data):
    result = ([], [])
    for (i, line) in enumerate(data):
        parts = line.strip().split()
        if len(parts) != 2:
            raise ValueError('Invalid row at %s with value "%s"' % (i, line))
        else:
            result[0].append(int(parts[0]))
            result[1].append(int(parts[1]))
    return sorted(result[0]), sorted(result[1])

class Day1(Template):
    def __init__(self, func, data=0):
        super().__init__(1, func, parse_data, data)

    @staticmethod
    def part_1(data=0):
        return Part1(data)

    @staticmethod
    def part_2(data=0):
        return Part2(data)


class Part1(Day1):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def __func(self):
        list_1 = self.data[0]
        list_2 = self.data[1]
        diff = 0
        for i in range(len(list_1)):
            diff += abs(list_1[i] - list_2[i])
        return diff


class Part2(Day1):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def __func(self):
        list_1 = self.data[0]
        list_2 = self.data[1]
        similarity = 0
        idx1 = idx2 = 0
        while idx1 < len(list_1) and idx2 < len(list_1):
            val1 = list_1[idx1]
            val2 = list_2[idx2]
            idx1_count = 0
            idx2_count = 0
            if val1 == val2:
                while idx1 < len(list_1) and list_1[idx1] == val2:
                    idx1 += 1
                    idx1_count += 1
                while idx2 < len(list_2) and val1 == list_2[idx2]:
                    idx2 += 1
                    idx2_count += 1
            elif val1 < val2:
                idx1 += 1
            else:
                idx2 += 1
            similarity += val1 * idx1_count * idx2_count
        return similarity
