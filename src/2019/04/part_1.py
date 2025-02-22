def read_data(input_data):
    first, second = input_data.split("-")
    return first, second


def run(input_data) -> int:
    first, second = read_data(input_data)
    values = [
        value
        for value in range(int(first), int(second) + 1)
        if is_valid(list(str(value)))
    ]
    return len(values)


def is_valid(values):
    last_num = None
    for value in values:
        if last_num is not None and last_num > value:
            return False
        last_num = value
    return contains_duplicate(values)


def contains_duplicate(values):
    last_num = None
    for value in values:
        if last_num is not None and last_num == value:
            return True
        last_num = value
    return False


if __name__ == "__main__":
    print(run("245182-790572"))
