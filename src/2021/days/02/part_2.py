def read_data(input_data):
    return [row.split(" ") for row in input_data.splitlines()]


def run(input_data: str):
    values = read_data(input_data)
    horizontal = depth = aim = 0
    for direction, value in values:
        value = int(value)
        match direction:
            case "down":
                aim += value
            case "up":
                aim -= value
            case "forward":
                depth += aim * value
                horizontal += value
    return horizontal * depth


if __name__ == "__main__":
    print(run(open("src/2021/data/days/02/data", "r").read()))
