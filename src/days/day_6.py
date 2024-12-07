from src.days.template import Template


class Guard:
    def __init__(self, pos):
        self.pos = pos
        self.direction = -1j

    def turn(self):
        self.direction *= 1j

    def move(self, value):
        self.pos = value

    def next_move_target(self):
        return self.pos + self.direction


def parse_data(data):
    obstacles: set[complex] = set()
    row_limit = len(data)
    col_limit = len(data[0].strip())
    guard = None
    for (row_idx, row) in enumerate(data):
        for (col_idx, val) in enumerate(row):
            if val == '#':
                obstacles.add(col_idx + row_idx * 1j)
            elif val == '^':
                guard = Guard(col_idx + row_idx * 1j)
    return guard, obstacles, row_limit, col_limit


class Day6(Template):
    def __init__(self, func, data=0):
        super().__init__(6, func, parse_data, data)

    @staticmethod
    def part_1(data=0):
        return Part1(data)

    @staticmethod
    def part_2(data=0):
        return Part2(data)


class Part1(Day6):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def __func(self):
        guard, obstacles, height, width = self.data
        reached_locations: set[complex] = {guard.pos}
        while True:
            next_move = guard.next_move_target()
            if next_move in obstacles:
                guard.turn()
            elif 0 <= next_move.imag < height and 0 <= next_move.real < width:
                guard.move(next_move)
                reached_locations.add(next_move)
            else:
                return len(reached_locations)


class Part2(Day6):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def __func(self):
        pass
