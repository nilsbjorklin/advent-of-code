def read_data(input_data):
    return {int(row.strip()) for row in input_data.splitlines()}


def run(input_data, target_value):
    values = read_data(input_data)
    for value1 in values:
        for value2 in values:
            pair_sum = value1 + value2
            matching_value = target_value - pair_sum
            if matching_value in values:
                return value1 * value2 * matching_value


if __name__ == "__main__":
    print(run(open("data", "r").read(), 2020))
