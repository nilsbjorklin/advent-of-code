from src.days.template import Template


def fetch_data():
    return [3, 5, 6, 1], [3, 5, 6, 1]


def sort_data(data):
    return sorted(data[0]), sorted(data[1])


class Day1(Template):
    def __init__(self, data=fetch_data()):
        super().__init__(1, sort_data(data), self.__func)

    def __func(self):
        list_1 = self.data[0]
        list_2 = self.data[1]
        diff = 0
        print(list_1, list_2)
        for i in range(len(list_1)):
            diff += abs(list_1[i] - list_2[i])
        return diff
