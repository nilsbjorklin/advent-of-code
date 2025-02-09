def read_data(input_data: str) -> list[list[set]]:
    return [
        [{*answer} for answer in group.splitlines()]
        for group in input_data.split("\n\n")
    ]


def run(input_data: str):
    groups: list[list[set]] = read_data(input_data)
    return sum([len(set.intersection(*group)) for group in groups])


if __name__ == "__main__":
    print(run(open("data", "r").read()))
