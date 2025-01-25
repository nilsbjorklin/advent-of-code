def read_data(input_data):
    return len(input_data.splitlines()[0]), [row for row in input_data.splitlines()]


def run(input_data: str):
    cols_len, values = read_data(input_data)
    oxygen = c02 = values
    for index in range(cols_len):
        oxygen = filter_values(index, oxygen, True)
        c02 = filter_values(index, c02, False)
    return int(oxygen[0], 2) * int(c02[0], 2)


def filter_values(index, values, boolean):
    if len(values) == 1:
        return values
    ones = sum([int(value[index]) for value in values])
    return [
        value
        for value in values
        if (value[index] == ("1" if ones >= len(values) - ones else "0")) == boolean
    ]


if __name__ == "__main__":
    print(run(open("src/2021/data/days/03/data", "r").read()))
