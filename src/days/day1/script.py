from src.days.template import Template


def fetch_data():
    f = open('data/days/day1/data', 'r')
    data = ([], [])
    for (i, line) in enumerate(f.readlines()):
        parts = line.strip().split()
        if len(parts) != 2:
            raise ValueError('Invalid row at %s with value "%s"' % (i, line))
        else:
            data[0].append(int(parts[0]))
            data[1].append(int(parts[1]))
    return data


def sort_data(data):
    return sorted(data[0]), sorted(data[1])


class Day1(Template):
    def __init__(self, data=0):
        if data == 0:
            data = fetch_data()
        super().__init__(1, sort_data(data), self.__func)

    def __func(self):
        list_1 = self.data[0]
        list_2 = self.data[1]
        diff = 0
        for i in range(len(list_1)):
            diff += abs(list_1[i] - list_2[i])
        return diff
