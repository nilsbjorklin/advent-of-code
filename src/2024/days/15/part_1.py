from typing import Union


def read_data(input_data) -> Union[complex, dict[set], list[complex]]:
    values = ["@", "#", "O"]
    move_values = {"<": -1, "^": -1j, ">": 1, "v": 1j}
    grid_data, move_data = input_data.split("\n\n")
    grid = {
        char: {
            col_idx + row_idx * 1j
            for row_idx, row in enumerate(grid_data.strip().splitlines()[1:][:-1])
            for col_idx, c in enumerate(row.strip()[1:][:-1])
            if c == char
        }
        for char in values
    }
    return (
        len(grid_data.splitlines()[0]) - 2 + (len(grid_data.splitlines()) - 2) * 1j,
        list(grid.pop(values[0]))[0],
        grid,
        [
            move_values[move]
            for line in move_data.strip().splitlines()
            for move in line.strip()
        ],
    )


def run(input_data: str):
    size, robot, grid, moves = read_data(input_data)

    for move_direction in moves:
        robot = try_move(size, robot, move_direction, grid)

    return sum([int(box.imag + 1) * 100 + int(box.real + 1) for box in grid["O"]])


def try_move(size, pos, move_direction, grid, box=False):
    next_pos = pos + move_direction
    if 0 > next_pos.real or next_pos.real >= size.real:
        return pos
    elif 0 > next_pos.imag or next_pos.imag >= size.imag:
        return pos
    elif next_pos in grid["#"]:
        return pos
    elif next_pos in grid["O"]:
        next_box = try_move(size, next_pos, move_direction, grid, True)
        if next_box == next_pos:
            return pos
    if box:
        grid["O"].remove(pos)
        grid["O"].add(next_pos)
    return next_pos


if __name__ == "__main__":
    print(run(open("src/2024/data/days/15/data", "r").read()))
