directions = ["E", "S", "W", "N"]


def read_data(input_data: str) -> list:
    instructions = []
    for line in input_data.splitlines():
        instructions.append((line[0], int(line[1:])))
    return instructions


def run(input_data: str) -> int:
    instructions = read_data(input_data)
    direction = 0
    x = y = 0
    for command, value in instructions:
        if command == "F":
            command = directions[direction]
        match command:
            case "N":
                y -= value
            case "S":
                y += value
            case "E":
                x += value
            case "W":
                x -= value
            case _:
                steps = value // 90
                if command == "L":
                    steps = -steps
                direction = (direction + steps) % 4
    return abs(x) + abs(y)


if __name__ == "__main__":
    print(run(open("data", "r").read()))
