def read_data(input_data):
    return [int(row.strip()) for row in input_data.splitlines()]


def run(input_data) -> int:
    values = read_data(input_data)
    index = 0
    frequency = 0
    previous_results = {0}
    while frequency + values[index % len(values)] not in previous_results:
        frequency += values[index % len(values)]
        previous_results.add(frequency)
        index += 1
    return frequency + values[index % len(values)]


if __name__ == "__main__":
    print(run(open("data", "r").read()))
