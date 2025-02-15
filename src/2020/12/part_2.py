directions = ["E", "S", "W", "N"]


def read_data(input_data: str) -> list:
    instructions = []
    for line in input_data.splitlines():
        instructions.append((line[0], int(line[1:])))
    return instructions


def run(input_data: str) -> int:
    instructions = read_data(input_data)
    waypoint_x = 10
    waypoint_y = -1
    x = y = 0
    for command, value in instructions:
        match command:
            case "F":
                x += waypoint_x * value
                y += waypoint_y * value
            case "N":
                waypoint_y -= value
            case "S":
                waypoint_y += value
            case "E":
                waypoint_x += value
            case "W":
                waypoint_x -= value
            case _:
                waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, command, value)
    return abs(x) + abs(y)


def rotate(waypoint_x, waypoint_y, command, value):
    steps = value // 90
    if command == "L":
        steps = -steps
    match steps % 4:
        case 1:
            return -waypoint_y, waypoint_x
        case 2:
            return -waypoint_x, -waypoint_y
        case 3:
            return waypoint_y, -waypoint_x


if __name__ == "__main__":
    print(run(open("data", "r").read()))
