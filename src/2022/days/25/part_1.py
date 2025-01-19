from functools import reduce

value_mapper = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
    2: "2",
    1: "1",
    0: "0",
    -1: "-",
    -2: "=",
}


def read_data(input_data):
    return [
        [value_mapper[char] for row in rows for char in row]
        for rows in input_data.splitlines()
    ]


def run(input_data):
    rows = read_data(input_data)
    total = reduce(lambda a, b: a + b, [SNAFU_to_decimal(vals) for vals in rows], 0)
    return decimal_to_SNAFU(total)


def SNAFU_to_decimal(SNAFU):
    result = 0
    row_len = len(SNAFU)
    for index in range(row_len):
        digit_value = 5 ** (row_len - index - 1)
        result += digit_value * SNAFU[index]
    return result


def decimal_to_SNAFU(decimal_number):
    SNAFU = []
    while decimal_number:
        divisor = decimal_number // 5
        distance = decimal_number - divisor * 5
        if distance > 2:
            distance = 5 - distance
            divisor += 1
        closes_num = divisor * 5
        difference = decimal_number - closes_num
        SNAFU.append(value_mapper[difference])
        decimal_number = closes_num // 5
    return "".join(SNAFU[::-1])


if __name__ == "__main__":
    print(run(open("src/2022/data/days/25/data", "r").read()))
