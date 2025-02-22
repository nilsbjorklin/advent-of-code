def read_data(input_data):
    return [int(row.strip()) for row in input_data.splitlines()]


def run(input_data) -> int:
    values = read_data(input_data)
    result = 0
    for value in values:
        while value > 0:
            value = max((value // 3) - 2, 0)
            result += value
    return result


if __name__ == "__main__":
    assert run("""14""") == 2
    assert run("""1969""") == 966
    assert run("""100756""") == 50346
    print(run(open("data", "r").read()))
