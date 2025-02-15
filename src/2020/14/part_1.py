def read_data(input_data: str) -> list:
    sections = []
    lines = input_data.splitlines()
    index = 0
    while index < len(lines):
        mask = lines[index].split(" = ")[1]
        zero_mask = ""
        one_mask = ""
        for char in mask:
            zero_mask += "1" if char == "X" else char
            one_mask += "0" if char == "X" else char
        section = []
        index += 1
        while index < len(lines) and not lines[index].startswith("mask"):
            address, value = lines[index].split(" = ")
            section.append((int(address[4:-1]), int(value)))
            index += 1
        sections.append((int(zero_mask, base=2), int(one_mask, base=2), section))
    return sections


def run(input_data: str) -> int:
    sections = read_data(input_data)
    registers = {}
    for zero_mask, one_mask, values in sections:
        for address, value in values:
            registers[address] = zero_mask & value | one_mask
    return sum(registers.values())


if __name__ == "__main__":
    print(run(open("data", "r").read()))
