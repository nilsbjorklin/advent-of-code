from functools import lru_cache
import re


tiles = []
walls = []
directions = [1, 1j, -1, -1j]


def read_data(input_data):
    global tiles, walls
    start = None
    instructions = []
    grid, instruction_str = input_data.split("\n\n")
    for digit, turn in re.compile(r"(\d+)(\w)?").findall(instruction_str):
        if turn == "L":
            turn = -1
        elif turn == "R":
            turn = 1
        else:
            turn = 0
        instructions.append((int(digit), turn))
    for y, row in enumerate(grid.splitlines()):
        for x, char in enumerate(row):
            pos = complex(x, y)
            if char == ".":
                tiles.append(pos)
                if start is None:
                    start = pos
            elif char == "#":
                tiles.append(pos)
                walls.append(pos)
                if start is None:
                    start = pos
    return start, instructions


def run(input_data):
    start, instructions = read_data(input_data)
    direction_id = 0
    pos = start
    for steps, turn in instructions:
        pos = move(steps, directions[direction_id], pos)
        direction_id = (turn + direction_id) % 4
    return 1000 * int(pos.imag + 1) + 4 * int(pos.real + 1) + direction_id


@lru_cache
def move(steps, direction, pos):
    for _ in range(steps):
        next_pos = pos + direction
        if next_pos not in tiles:
            next_pos = wrap_around(direction, pos)
        if next_pos in walls:
            return pos
        if next_pos in tiles:
            pos = next_pos
    return pos


@lru_cache
def wrap_around(direction, pos):
    reverse_direction = direction * -1
    next_pos = pos
    while next_pos + reverse_direction in tiles:
        next_pos += reverse_direction
    return next_pos


if __name__ == "__main__":
    print(run(open("src/2022/data/days/22/data", "r").read()))
