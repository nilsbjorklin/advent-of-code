def read_data(input_data):
    return [int(v) for v in input_data.split(",")]


def run(input_data) -> None:
    values = read_data(input_data)
    value, idx_res = 1, values[1]
    values[idx_res] = value
    index = 2
    while index < len(values):
        number = str(values[index]).zfill(5)
        op_code = int(number[3:])
        match op_code:
            case 99:
                break
            case 1:
                idx_1, idx_2, idx_res = get_numbers(index, number[0:3], values)
                values[idx_res] = values[idx_1] + values[idx_2]
                index += 4
            case 2:
                idx_1, idx_2, idx_res = get_numbers(index, number[0:3], values)
                values[idx_res] = values[idx_1] * values[idx_2]
                index += 4
            case 3:
                value, idx_res = values[index - 1], values[index + 1]
                values[idx_res] = value
                index += 2
            case 4:
                print(values[values[index + 1]])
                index += 2


def get_numbers(index, parameter_mode, values):
    return [
        index + i + 1 if mode else values[index + i + 1]
        for i, mode in enumerate(map(bool, map(int, reversed(parameter_mode))))
    ]


if __name__ == "__main__":
    run(open("data").read())
