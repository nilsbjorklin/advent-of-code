def read_data(input_data):
    return [
        [tuple(map(int, elf.split("-"))) for elf in row.split(",")]
        for row in input_data.splitlines()
    ]


def run(input_data: list[str]):
    elf_pairs = read_data(input_data)
    return sum(
        [(min(min(elf_pair)), max(max(elf_pair))) in elf_pair for elf_pair in elf_pairs]
    )


if __name__ == "__main__":
    print(run(open("src/2022/data/days/04/data", "r").read()))
