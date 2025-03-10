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
    has_duplicate = False
    for value in values:
        if last_num is not None:
            if last_num > value:
                return False
            elif last_num == value:
                has_duplicate = True
        last_num = value
    return has_duplicate


if __name__ == "__main__":
    print(run("245182-790572"))
