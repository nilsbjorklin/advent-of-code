def read_data(input_data: str) -> list[list[str]]:
    return [group.splitlines() for group in input_data.split("\n\n")]


def run(input_data: str):
    groups: list[list[str]] = read_data(input_data)
    return sum(len({char for answer in group for char in answer}) for group in groups)


if __name__ == "__main__":
    print(run(open("data", "r").read()))
