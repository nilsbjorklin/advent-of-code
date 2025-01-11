from collections import deque
from functools import lru_cache
import numpy as np
import networkx as nx

shapes = [
    [0, 1, 2, 3],
    [1j, 1 + 1j, 2 + 1j, 1, 1 + 2j],
    [0, 1, 2, 2 + 1j, 2 + 2j],
    [0j, 1j, 2j, 3j],
    [0, 1, 1j, 1 + 1j],
]
shape_width = [3, 2, 2, 0, 1]


def read_data(input_data):
    return deque([-1 if char == "<" else 1 for char in input_data])


@lru_cache
def get_rock(index):
    return np.array(shapes[index]), shape_width[index]


def run(input_data, num_rocks):
    moves = read_data(input_data)
    index = 0
    rock = None
    move_index = 0
    print_output = []
    floor = np.array([complex(i, 0) for i in range(7)])
    floor_offset = 0
    offset_changes = 0
    while index < num_rocks:
        if rock is None:
            mod_index = index % 5
            rock, rock_width = get_rock(mod_index)
            highest_rock = max(map(lambda x: int(x.imag), floor))
            rock_pos = complex(2, highest_rock + 4)
        if 183 <index < 185 and index % 1 == 0:
            print(f"{index=}, {move_index=}")
        move = moves[move_index % len(moves)]
        next_pos = rock_move(move, rock, rock_width, rock_pos, floor)
        if rock_pos != next_pos:
            rock_pos = next_pos
        rock_pos = next_pos
        move_index += 1

        rock_pos, stuck = rock_fall(rock, rock_pos, floor)
        if stuck:
            floor = build_floor(tuple(floor), tuple(rock_pos + rock))
            lowest_floor = min(map(lambda x: int(x.imag), floor))
            if lowest_floor != 0:
                    
                offset_changes += 1
                """print_output += print_rocks(
                    floor, floor_offset, max(map(lambda x: int(x.imag), floor))
                )"""
                floor = np.add(floor, complex(0, -lowest_floor))
                floor_offset += lowest_floor
                """print_output += print_rocks(
                    floor, floor_offset, max(map(lambda x: int(x.imag), floor))
                )"""
            highest_rock = max(map(lambda x: int(x.imag), floor))
            index += 1
            rock = None
            """if 186 <index < 189 and index % 1 == 0:
                print_output += print_rocks(
                    floor, floor_offset, max(map(lambda x: int(x.imag), floor))
                )
                print(index, max(map(lambda x: int(x.imag), floor)) + floor_offset)"""
    for output in print_output:
        print(output)
    return max(map(lambda x: int(x.imag), floor)) + floor_offset

@lru_cache
def build_floor(floor, rocks):
    all_rocks = np.concatenate((floor, rocks))
    new_floor = []
    for i in range(7):
        prev_rock = None
        for rock in [rock for rock in all_rocks if rock.real == i]:
            if prev_rock is None or prev_rock.imag < rock.imag:
                prev_rock = rock
        new_floor.append(prev_rock)
    graph = nx.Graph()
    directions = [1j, 1 + 1j, 1, 1 - 1j, -1j, -1 - 1j, -1]
    for rock in all_rocks:
        for direction in directions:
            next_rock = rock + direction
            if next_rock in all_rocks:
                graph.add_edge(rock, next_rock)
    return list({node for i in range(6) for node in nx.shortest_path(graph, new_floor[i], new_floor[i + 1])})


def rock_move(direction, rock, rock_width, rock_pos, floor):
    if rock_step(direction, rock_pos.real, rock_width):
        next_pos = rock_pos + direction
        if no_collision(tuple(next_pos + rock), tuple(floor)):
            return next_pos
    return rock_pos

@lru_cache
def rock_step(direction, rock_x, rock_width):
    next_x = rock_x + direction
    return 0 <= next_x and next_x + rock_width < 7


def rock_fall(rock, rock_pos, floor):
    next_pos = rock_pos - 1j
    if no_collision(tuple(next_pos + rock), tuple(floor)):
        return next_pos, False
    return rock_pos, True


@lru_cache
def no_collision(rock, floor):
    return len(set(floor).intersection(set(rock))) == 0


def print_rocks(floor, floor_offset, highest_rock, current_rock=()):
    rows = []
    for y in range(highest_rock + 2):
        output = f"{str(y + (floor_offset)).zfill(2)} |"
        for x in range(7):
            if complex(x, y) in current_rock:
                output += "@"
            elif complex(x, y) in floor:
                output += "#"
            else:
                output += "."
        output += "|"
        rows.append(output)
    rows.append("")
    return rows[::-1]


if __name__ == "__main__":
    print(run(open("src/2022/data/days/17/data", "r").read(), 2022))
