def read_data(input_data):
    return len(input_data.splitlines()[0]), [row for row in input_data.splitlines()]


def run(input_data: str):
    cols_len, values = read_data(input_data)
    gamma = ""
    for index in range(cols_len):
        col_sum = sum([int(value[index]) for value in values])
        gamma += "1" if col_sum > len(values) // 2 else "0"
    gamma = int(gamma, 2)
    return gamma * (2**cols_len - gamma - 1)


if __name__ == "__main__":
    print(run(open("src/2021/data/days/03/data", "r").read()))
