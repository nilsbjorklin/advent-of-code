from collections import deque
from functools import lru_cache, reduce


blizzard_mapping = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}
char_mapping = {(1, 0): ">", (-1, 0): "<", (0, 1): "v", (0, -1): "^"}
possible_moves = [1, -1, 0, 1j, -1j]
height = width = 0
start = end = 0
blizzards = []


def read_data(input_data):
    global height, width
    height = len(input_data.splitlines()) - 2
    width = len(input_data.splitlines()[0]) - 2
    global start, end
    start = complex(0, -1)
    end = complex(width - 1, height)
    global blizzards
    blizzards = [
        ((x - 1, y - 1), blizzard_mapping[char])
        for y, row in enumerate(input_data.splitlines())
        for x, char in enumerate(row)
        if char in blizzard_mapping
    ]


def run(input_data):
    read_data(input_data)
    return reduce(
        lambda result, start_end_pos: find_first_path(*start_end_pos, result),
        [(start, end), (end, start), (start, end)],
        0,
    )


def find_first_path(start, end, start_time=0):
    path = deque([(start, start_time)])
    visited = set()
    shortest_path_found = None
    while len(path) != 0:
        pos, time = path.popleft()
        if shortest_path_found is None or time <= shortest_path_found:
            if pos == end:
                shortest_path_found = time - 1
            else:
                pos_change = (time % width, time % height)
                if (pos, pos_change) not in visited:
                    visited.add((pos, pos_change))
                    for move in next_positions(pos, pos_change):
                        path.append((move, time + 1))
    return shortest_path_found


@lru_cache
def next_positions(pos, pos_change):
    return [
        pos + move for move in possible_moves if valid_position(pos + move, pos_change)
    ]


@lru_cache
def valid_position(new_pos, pos_change):
    inside = start == new_pos or end == new_pos
    if not inside:
        inside = 0 <= new_pos.real <= width - 1 and 0 <= new_pos.imag <= height - 1
    if inside:
        return new_pos not in blizzards_at_time(pos_change)
    return False


@lru_cache
def blizzards_at_time(pos_change):
    return {calculate_blizzard(pos_change, blizzard) for blizzard in blizzards}


@lru_cache
def calculate_blizzard(pos_change, blizzard):
    pos, change = blizzard
    if pos_change == (0, 0):
        return complex(*pos)
    return complex(
        (pos[0] + change[0] * pos_change[0]) % width,
        (pos[1] + change[1] * pos_change[1]) % height,
    )


if __name__ == "__main__":
    print(run(open("src/2022/data/days/24/data", "r").read()))
