from copy import deepcopy

from src.days.template import Template


class Guard:
    def __init__(self, pos):
        self.pos = pos
        self.direction = -1j
        self.turns = []
        self.path = set()
        self.path.add(pos)

    def turn(self):
        self.direction *= 1j
        self.turns.append(self.pos)

    def get_latest_turns(self, num=3):
        return self.turns[-num:]

    def move(self, value):
        self.pos = value
        self.path.add(value)

    def steps_to_path(self, destination):
        steps_needed: complex = destination - self.pos
        result = []
        if steps_needed.imag:
            num_steps = abs(steps_needed.imag)
            direction = 1j if num_steps == steps_needed.imag else -1j
        else:
            num_steps = abs(steps_needed.real)
            direction = 1 if num_steps == steps_needed.real else -1
        for i in range(int(num_steps)):
            result.append(direction)
        return result

    def next_move_target(self):
        return self.pos + self.direction


def parse_data(data):
    obstacles: set[complex] = set()
    row_limit = len(data)
    col_limit = len(data[0].strip())
    pos: complex = 0 + 0j
    for (row_idx, row) in enumerate(data):
        for (col_idx, val) in enumerate(row):
            if val == '#':
                obstacles.add(col_idx + row_idx * 1j)
            elif val == '^':
                pos = col_idx + row_idx * 1j
    return pos, obstacles, row_limit, col_limit


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
        pos, obstacles, height, width = self.data
        direction = -1j
        path = set()
        while 0 <= pos.real < width and 0 <= pos.imag < height:
            if pos + direction in obstacles:
                direction *= 1j
            else:
                path.add(pos)
                pos += direction
        return len(set(path))


class Part2(Day6):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def calculate_path(self):
        pos, obstacles, height, width = deepcopy(self.data)
        direction = -1j
        path = []
        while 0 <= pos.real < width and 0 <= pos.imag < height:
            if pos + direction in obstacles:
                direction *= 1j
            else:
                pos += direction
                if pos not in path:
                    path.append(pos)
        return path

    def __func(self):
        path = self.calculate_path()
        pos, obstacles, height, width = self.data
        num_obstacles = 0
        for i, location in enumerate(path):
            new_obstacles = deepcopy(obstacles)
            new_obstacles.add(location)
            if check_looping(pos, new_obstacles, height, width):
                num_obstacles += 1
        return num_obstacles


def check_looping(pos, obstacles, height, width):
    direction = -1j
    memory = set()
    dir_count = 0
    while 0 <= pos.real < width and 0 <= pos.imag < height:
        if (pos, direction) in memory:
            return True
        if (pos + direction) in obstacles:
            memory.add((pos, direction))
            direction *= 1j
        else:
            dir_count += 1
            pos += direction
    return False
