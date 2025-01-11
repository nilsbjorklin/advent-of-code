def read_data(input_data):
    return [
        [tuple(map(int, elf.split("-"))) for elf in row.split(",")]
        for row in input_data.splitlines()
    ]


def run(input_data: list[str]):
    elf_pairs = read_data(input_data)
    return sum(not (e0[1] < e1[0] or e1[1] < e0[0]) for e0, e1 in elf_pairs)


if __name__ == "__main__":
    print(run(open("src/2022/data/days/04/data", "r").read()))
