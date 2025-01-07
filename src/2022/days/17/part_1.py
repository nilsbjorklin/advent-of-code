from collections import deque
import numpy as np

shapes = [
    [0, 1, 2, 3],
    [-1j, 1 - 1j, 2 - 1j, 1, 1 - 2j],
    [0, 1, 2, 2 - 1j, 2 - 2j],
    [0j, -1j, -2j, -3j],
    [0, 1, -1j, 1 - 1j],
]
shape_sizes = [
    (4, 1),
    (3, 3),
    (3, 3),
    (1, 4),
    (2, 2),
]


def read_data(input_data):
    return deque([-1 if char == "<" else 1 for char in input_data])


def run(input_data, num_rocks):
    moves = read_data(input_data)
    highest_rock = 0
    index = 0
    rock = None
    move_index = 0
    placed_rocks = set()
    while index < num_rocks:
        if rock is None:
            rock = np.array(shapes[index % 5])
            rock_shape = shape_sizes[index % 5]
            rock_pos = complex(2, -(3 - highest_rock))
        move = moves[move_index % len(moves)]
        rock_pos = rock_move(move, rock, rock_shape, rock_pos, placed_rocks)
        move_index += 1

        rock_pos, stuck = rock_fall(rock, rock_pos, placed_rocks)
        if stuck:
            placed_rocks.update(rock_pos + rock)
            highest_rock = int(min(highest_rock, rock_pos.imag - rock_shape[1]))
            index += 1
            rock = None
    return abs(highest_rock)


def rock_move(direction, rock, rock_shape, rock_pos, placed_rocks):
    next_pos = rock_pos + direction
    if 0 <= next_pos.real and next_pos.real + rock_shape[0] <= 7:
        if len(placed_rocks.intersection(next_pos + rock)) == 0:
            return next_pos
    return rock_pos


def rock_fall(rock, rock_pos, placed_rocks):
    next_pos = rock_pos + 1j
    if 0 >= next_pos.imag:
        if len(placed_rocks.intersection(next_pos + rock)) == 0:
            return next_pos, False
    return rock_pos, True


if __name__ == "__main__":
    print(run(open("src/2022/data/days/17/data", "r").read(), 2022))
