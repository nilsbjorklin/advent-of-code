from copy import copy


def read_data(input_data):
    return [
        (index, int(row.strip())) for index, row in enumerate(input_data.splitlines())
    ]


def run(input_data):
    numbers = read_data(input_data)
    original = copy(numbers)
    for number in original:
        index = numbers.index(number)
        value = numbers.pop(index)
        numbers.insert((index + value[1]) % len(numbers), value)
    numbers = list(map(lambda x: x[1], numbers))
    zero_index = numbers.index(0)
    return sum(
        [numbers[(i + zero_index) % len(numbers)] for i in range(1000, 3001, 1000)]
    )


if __name__ == "__main__":
    print(run(open("src/2022/data/days/20/data", "r").read()))
