import copy

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
        while True:
            next_move = guard.next_move_target()
            if next_move in obstacles:
                guard.turn()
            elif 0 <= next_move.imag < height and 0 <= next_move.real < width:
                guard.move(next_move)
            else:
                return len(guard.path)


def path_is_looped(guard: Guard, obstacles: list[complex], height: int, width: int):
    while True:
        next_move = guard.next_move_target()
        if next_move in obstacles:
            guard.turn()
            last_two_turns = guard.get_latest_turns(2)
            if last_two_turns[0] in guard.turns and last_two_turns[1] in guard.turns:
                for i, turn in enumerate(guard.turns[:-2]):
                    if turn == last_two_turns[0]:
                        if guard.turns[i + 1] == last_two_turns[1]:
                            return True
        elif 0 <= next_move.imag < height and 0 <= next_move.real < width:
            guard.move(next_move)
        else:
            print(f'guard exit at {guard.pos}')
            return False


class Part2(Day6):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def __func(self):
        guard, obstacles, height, width = self.data
        new_obstacles = []
        while True:
            next_move = guard.next_move_target()
            if next_move in obstacles:
                guard.turn()
                turns = guard.get_latest_turns()
                if len(turns) == 3:
                    real = turns[0].real if turns[0].real != turns[1].real else turns[2].real
                    imag = turns[0].imag if turns[0].imag != turns[1].imag else turns[2].imag
                    new_obstacle = real + imag * 1j + guard.direction
                    if self.potential_obstacle(new_obstacle):
                        new_obstacles.append(new_obstacle)

            elif 0 <= next_move.imag < height and 0 <= next_move.real < width:
                guard.move(next_move)
            else:
                ''' for obstacle in new_obstacles:
                     image = []
                     for j in range(height):
                         row = []
                         for i in range(width):
                             if i + j * 1j in obstacle:
                                 if obstacle.index(i + j * 1j) == 3:
                                     row.append('O')
                                 else:
                                     row.append('X')
                             else:
                                 row.append('.')
                         row.append("")
                         image.append(''.join(row))
                     print('\n'.join(image), '\n')'''
                # self.potential_obstacle()
                last_turn = guard.get_latest_turns(1)[0]
                path = set()
                num_steps = int(abs((last_turn - guard.pos).imag + (last_turn - guard.pos).real)) + 1
                path.update(last_turn + step * + guard.direction for step in range(1, num_steps))
                for obstacle in path:
                    new_guard = copy.deepcopy(guard)
                    new_guard.pos = last_turn
                    if path_is_looped(new_guard, list(obstacles) + [obstacle], height, width):
                        new_obstacles.append(obstacle)
                    else:
                        print(f'invalid obstacle {obstacle}')
                image = []
                for j in range(height):
                    row = []
                    for i in range(width):
                        if i + j * 1j in guard.turns:
                            row.append(f"{guard.turns.index(i + j * 1j)}")
                        elif i + j * 1j in obstacles:
                            row.append('#')
                        else:
                            row.append('.')
                    row.append("")
                    image.append(''.join(row))
                print('\n'.join(image), '\n')
                print()
                return len(new_obstacles)

    def potential_obstacle(self, new_obstacle):
        guard, obstacles, _, _ = self.data
        if new_obstacle not in guard.path:
            path = set()
            num_steps = int(abs((new_obstacle - guard.pos).imag + (new_obstacle - guard.pos).real))
            path.update(guard.pos + step * guard.direction for step in range(1, num_steps))

            conflict = set(path).intersection(obstacles)

            if len(set(path).intersection(obstacles)) == 0:
                print(f'added obstacle at {new_obstacle}')
                return True
            else:
                print(f'did not add obstacle at {new_obstacle} due to conflict at {list(conflict)}')
        else:
            print(f'did not add obstacle at {new_obstacle} due to path already travelled')
        return False
