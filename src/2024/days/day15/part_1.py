def read_data(input_data):
    robot = 0
    moves = []
    walls = set()
    boxes = set()
    upper_wall = input_data[0]
    width = len(upper_wall) - 2
    height = 0
    parse_grid = True
    for row_idx, row in enumerate(input_data[1:]):
        if row == upper_wall:
            height = row_idx
            continue
        if len(row.strip()) == 0:
            parse_grid = False
            continue
        if parse_grid:
            for col_idx in range(width):
                pos = col_idx + row_idx * 1j
                match row.strip()[col_idx + 1]:
                    case '@':
                        robot = pos
                    case '#':
                        walls.add(pos)
                    case 'O':
                        boxes.add(pos)
        else:
            for direction in row:
                match direction:
                    case '<':
                        moves.append(-1)
                    case '^':
                        moves.append(-1j)
                    case '>':
                        moves.append(1)
                    case 'v':
                        moves.append(1j)
    return width + height * 1j, robot, moves, walls, boxes


def run(input_data: list[str]):
    size, robot, moves, walls, boxes = read_data(input_data)
    for move_direction in moves:
        robot = move(size, robot, move_direction, walls, boxes)

    return sum([int(box.imag + 1) * 100 + int(box.real + 1) for box in boxes])


def move(size, pos, move_direction, walls, boxes, box=False):
    next_pos = pos + move_direction
    if 0 > next_pos.real or next_pos.real >= size.real:
        return pos
    elif 0 > next_pos.imag or next_pos.imag >= size.imag:
        return pos
    elif next_pos in walls:
        return pos
    elif next_pos in boxes:
        next_box = move(size, next_pos, move_direction, walls, boxes, True)
        if next_box == next_pos:
            return pos
    if box:
        boxes.remove(pos)
        boxes.add(next_pos)
    return next_pos


if __name__ == '__main__':
    print(run(open('data', 'r').readlines()))
