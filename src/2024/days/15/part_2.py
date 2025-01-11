from collections import defaultdict

boxes = defaultdict(complex)
walls = set()
robot = 0
size = 0


def read_data(input_data) -> list:
    global boxes
    global walls
    global robot
    global size

    move_values = {"<": -1, "^": -1j, ">": 1, "v": 1j}
    grid_data, move_data = input_data.split("\n\n")
    for row_idx, row in enumerate(grid_data.strip().splitlines()[1:][:-1]):
        for col_idx, c in enumerate(row.strip()[1:][:-1]):
            pos = col_idx * 2 + row_idx * 1j
            if c == "@":
                robot = pos
            elif c == "#":
                walls.add(pos)
                walls.add(pos + 1)
            elif c == "O":
                boxes[pos] = pos + 1
                boxes[pos + 1] = pos

    size = (len(grid_data.splitlines()[0]) - 2) * 2 + (
        len(grid_data.splitlines()) - 2
    ) * 1j

    return [move_values[move] for move in move_data.strip().replace("\n", "")]


def run(input_data: str):
    moves = read_data(input_data)
    for move in moves:
        move_robot(move)
    return sum(
        [
            (
                (100 * (int(box.imag) + 1) + int(box.real) + 2)
                if box - boxes[box] == -1
                else 0
            )
            for box in boxes
        ]
    )


def move_robot(move):
    global robot
    next_pos = robot + move
    status, obstacle = next_pos_status(next_pos)
    if status:
        robot = next_pos
        return True
    elif obstacle is not None and move_box(next_pos, move):
        robot = next_pos
        return True
    return False


def move_box(initial_pos, move_direction):
    second_pos = boxes.pop(initial_pos)
    first_pos = boxes.pop(second_pos)
    pos_list = [first_pos, second_pos]
    next_pos_list = []
    for pos in pos_list:
        next_pos = pos + move_direction
        status, obstacle = next_pos_status(next_pos)
        if status:
            next_pos_list.append(next_pos)
        elif obstacle is None:
            next_pos_list = pos_list
            break
        else:
            if move_box(next_pos, move_direction):
                next_pos_list.append(next_pos)
            else:
                next_pos_list = pos_list
                break
    boxes[next_pos_list[0]] = next_pos_list[1]
    boxes[next_pos_list[1]] = next_pos_list[0]

    return next_pos_list != pos_list


def next_pos_status(pos):
    if 0 > pos.real or pos.real >= size.real:
        return False, None
    elif 0 > pos.imag or pos.imag >= size.imag:
        return False, None
    elif pos in walls:
        return False, None
    elif pos in boxes:
        return False, boxes[pos]
    return True, None


if __name__ == "__main__":
    print(run(open("src/2024/data/days/15/data", "r").read()))
