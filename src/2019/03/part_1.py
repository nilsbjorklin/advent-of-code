directions = {"R": 1, "L": -1, "D": 1j, "U": -1j}


def read_data(input_data):
    lines = input_data.splitlines()
    first = lines[0].split(",")
    second = lines[1].split(",")
    return first, second


def run(input_data) -> int:
    first, second = read_data(input_data)
    return min(
        [
            int(abs(value.imag) + abs(value.real))
            for value in calculate(first).intersection(calculate(second))
        ]
    )


def calculate(values):
    positions = set()
    current_pos = 0
    for instruction in values:
        direction = directions[instruction[0]]
        steps = int(instruction[1:])
        for i in range(steps):
            current_pos += direction
            positions.add(current_pos)
    return positions


if __name__ == "__main__":
    first_test = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
    assert run(first_test) == 159

    second_test = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
    assert run(second_test) == 135
    print(run(open("data", "r").read()))
