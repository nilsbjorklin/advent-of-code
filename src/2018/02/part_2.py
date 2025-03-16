def read_data(input_data):
    return [row.strip() for row in input_data.splitlines()]


def run(input_data) -> int:
    values = read_data(input_data)
    for first_index, first_value in enumerate(values):
        for second_index in range(first_index + 1, len(values)):
            second_value = values[second_index]
            result = check_missmatch(first_value, second_value)
            if result:
                return result


def check_missmatch(first_value, second_value):
    invalid_counter = 0
    result = ""
    for char_index, first_char in enumerate(first_value):
        if first_char != second_value[char_index]:
            invalid_counter += 1
        else:
            result += first_char
        if invalid_counter > 1:
            return False
    return result


if __name__ == "__main__":
    print(run(open("data", "r").read()))
