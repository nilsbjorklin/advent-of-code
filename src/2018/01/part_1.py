def read_data(input_data):
    return [int(row.strip()) for row in input_data.splitlines()]


def run(input_data) -> int:
    values = read_data(input_data)
    return sum(values)


if __name__ == "__main__":
    print(run(open("data", "r").read()))
