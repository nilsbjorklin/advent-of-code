directions = {"R": 1, "L": -1, "D": 1j, "U": -1j}


def read_data(input_data):
    first, second = input_data.split("-")
    return first, second


def run(input_data) -> int:
    first, second = read_data(input_data)
    values = [value for value in range(int(first), int(second) + 1) if is_valid(value)]
    return len(values)


def is_valid(value):
    values = list(str(value))
    contains_duplicate = False
    for index in range(len(values) - 1):
        first, second = int(values[index]), int(values[index + 1])
        if second < first:
            return False
        elif first == second:
            contains_duplicate = True
    return contains_duplicate


if __name__ == "__main__":
    print(run("245182-790572"))
