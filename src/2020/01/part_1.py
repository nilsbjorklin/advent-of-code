def read_data(input_data):
    return {int(row.strip()) for row in input_data.splitlines()}


def run(input_data, target_value):
    values = read_data(input_data)
    for value in values:
        matching_value = target_value - value
        if matching_value in values:
            return value * matching_value


if __name__ == "__main__":
    print(run(open("data", "r").read(), 2020))
