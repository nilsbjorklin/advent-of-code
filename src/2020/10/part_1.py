def read_data(input_data: str) -> list[int]:
    return sorted(list(map(int, input_data.splitlines())))


def run(input_data: str) -> int:
    numbers: list[int] = read_data(input_data)
    last_number = 0
    joints = {1: 0, 2: 0, 3: 1}
    for number in numbers:
        joints[number - last_number] += 1
        last_number = number
    return joints[1] * joints[3]


if __name__ == "__main__":
    print(run(open("data", "r").read()))
