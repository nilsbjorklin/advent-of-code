from copy import deepcopy


def read_data(input_data):
    values = [int(row.strip()) for row in input_data.split(",")]
    return values


def run(input_data, target) -> int:
    values = read_data(input_data)
    for noun in range(100):
        for verb in range(100):
            values[1] = noun
            values[2] = verb
            if calculate(deepcopy(values)) == target:
                return 100 * noun + verb
    return -1


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
    print(run(open("data", "r").read(), 19690720))
