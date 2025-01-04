import numpy as np


def read_data(input_data):
    elf_pairs = [
        [list(map(int, elf.split("-"))) for elf in row.split(",")]
        for row in input_data.splitlines()
    ]
    return elf_pairs


def run(input_data: list[str]):
    elf_pairs = read_data(input_data)
    pairs_with_overlap = 0
    for elf_pair in elf_pairs:
        full_range = [np.min(elf_pair, axis=(1, 0)), np.max(elf_pair, axis=(1, 0))]
        if full_range in elf_pair:
            pairs_with_overlap += 1
    return pairs_with_overlap


if __name__ == "__main__":
    print(run(open("src/2022/data/days/04/data", "r").read()))
