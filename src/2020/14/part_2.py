def read_data(input_data: str) -> list:
    sections = []
    lines = input_data.splitlines()
    index = 0
    while index < len(lines):
        mask = lines[index].split(" = ")[1]
        values = []
        index += 1
        while index < len(lines) and not lines[index].startswith("mask"):
            address, value = lines[index].split(" = ")
            values.append((int(address[4:-1]), int(value)))
            index += 1
        sections.append(
            (
                int("".join(["0" if char == "X" else char for char in mask]), base=2),
                int("".join(["0" if char == "X" else "1" for char in mask]), base=2),
                [2 ** index for index, char in enumerate(mask[::-1]) if char == "X"],
                values,
            )
        )
    return sections


def run(input_data: str) -> int:
    sections = read_data(input_data)
    registers = {}
    for one_mask, zero_mask, floating, values in sections:
        floating_masks = [0]
        for number in floating:
            floating_masks += [result + number for result in floating_masks]
        for address, value in values:
            address = one_mask | address & zero_mask
            for floating_mask in floating_masks:
                registers[address + floating_mask] = value
    return sum(registers.values())


if __name__ == "__main__":
    print(run(open("data", "r").read()))
