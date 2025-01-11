def read_data(input_data):
    rucksacks = []
    for row in input_data.splitlines():
        row_len = len(row)
        compartment_1 = set(row[slice(0, row_len // 2)])
        compartment_2 = set(row[slice(row_len // 2, row_len)])
        rucksacks.append((compartment_1, compartment_2))
    return rucksacks


def run(input_data: list[str]):
    rucksacks = read_data(input_data)
    overlap_sum = 0
    for compartment_1, compartment_2 in rucksacks:
        char_val = ord(compartment_1.intersection(compartment_2).pop())
        char_val -= 38 if char_val < 97 else 96
        overlap_sum += char_val
    return overlap_sum


if __name__ == "__main__":
    print(run(open("src/2022/data/days/03/data", "r").read()))
