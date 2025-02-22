def read_data(input_data):
    return [int(row.strip()) for row in input_data.splitlines()]


def run(input_data) -> int:
    values = read_data(input_data)
    return sum(map(lambda a: (a // 3) - 2, values))


if __name__ == "__main__":
    assert run("""12""") == 2
    assert run("""14""") == 2
    assert run("""1969""") == 654
    assert run("""100756""") == 33583
    print(run(open("data", "r").read()))
