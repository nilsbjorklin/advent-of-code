def read_data(input_data):
    first, second = input_data.split("-")
    return first, second


def run(input_data) -> int:
    first, second = read_data(input_data)
    return len(
        [value for value in range(int(first), int(second) + 1) if is_valid(str(value))]
    )


def is_valid(values):
    last_num = None
    has_pair = False
    for value in values:
        if values.count(value) == 2:
            has_pair = True
        if last_num is not None and last_num > value:
            return False
        last_num = value
    return has_pair


if __name__ == "__main__":
    print(run("245182-790572"))
