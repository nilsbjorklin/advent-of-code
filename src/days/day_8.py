import itertools

from src.days.functions import print_2d
from src.days.template import Template

data = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............"
]


def parse_data(data):
    result = {}
    icon_dict = {}
    width = height = 0
    for height_idx, row in enumerate(data):
        width = len(row)
        height = len(data)
        for width_idx, letter in enumerate(row.strip()):
            if letter != '.':
                val = width_idx + height_idx * 1j
                if letter in result:
                    result[letter].append(val)
                else:
                    result[letter] = [width_idx + height_idx * 1j]
                icon_dict[val] = letter
    return result, icon_dict, width, height


class Day8(Template):
    def __init__(self, func, data=0):
        super().__init__(8, func, parse_data, data)

    @staticmethod
    def part_1(data=0):
        return Part1(data)

    @staticmethod
    def part_2(data=0):
        return Part2(data)


class Part1(Day8):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def antenna(self, a, b):
        _, _, width, height = self.data
        anti_node_1 = a * 2 - b
        if 0 <= int(anti_node_1.imag) < height and 0 <= int(anti_node_1.real) < width:
            return anti_node_1
        return None

    def __func(self):
        antennas, icon_dict, width, height = self.data
        nodes = set()
        for antenna_type in antennas.keys():
            indexes: list[int] = list(range(len(antennas[antenna_type])))
            orderings = list(itertools.permutations(indexes, 2))
            for order in orderings:
                nodes.add(self.antenna(antennas[antenna_type][order[0]], antennas[antenna_type][order[1]]))
        nodes = list(filter(None, nodes))
        for node in nodes:
            icon_dict[node] = '#'
        print_2d(width, height, icon_dict)
        return len(nodes)


class Part2(Day8):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def __func(self):
        pass
