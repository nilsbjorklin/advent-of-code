def read_data(input_data):
    values = [int(row.strip()) for row in input_data.split(",")]
    values[1] = 12
    values[2] = 2
    return values


def run(input_data) -> int:
    values = read_data(input_data)
    return calculate(values)


def calculate(values):
    index = 0
    while index < len(values):
        if values[index] == 1 or values[index] == 2:
            first_value = values[values[index + 1]]
            second_value = values[values[index + 2]]
            result_index = values[index + 3]
            if values[index] == 1:
                values[result_index] = first_value + second_value
            else:
                values[result_index] = first_value * second_value
        elif values[index] == 99:
            return values[0]
        index += 4


if __name__ == "__main__":
    assert calculate([1, 0, 0, 0, 99]) == 2
    assert calculate([2, 3, 0, 3, 99]) == 2
    assert calculate([2, 4, 4, 5, 99, 0]) == 2
    assert calculate([1, 1, 1, 4, 99, 5, 6, 0, 99]) == 30
    assert calculate([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == 3500
    print(run(open("data", "r").read()))
